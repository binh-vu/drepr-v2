from __future__ import annotations

from dataclasses import dataclass

from drepr.models.prelude import (
    Alignment,
    AttrId,
    Cardinality,
    DRepr,
    IdenticalAlign,
    RangeAlignment,
    ValueAlignment,
)


@dataclass
class DReprModelAlignments:
    desc: DRepr
    aligns: dict[tuple[AttrId, AttrId], list[Alignment]]

    @staticmethod
    def create(desc: DRepr) -> DReprModelAlignments:
        """Infer all possible alignments from the model."""
        aligns = {(src.id, tgt.id): [] for src in desc.attrs for tgt in desc.attrs}

        for a in desc.aligns:
            if isinstance(a, RangeAlignment):
                aligns[(a.source, a.target)] = [a]
                aligns[(a.target, a.source)] = [a.swap()]
            elif isinstance(a, ValueAlignment):
                aligns[(a.source, a.target)] = [a]
                aligns[(a.target, a.source)] = [a.swap()]
            elif isinstance(a, IdenticalAlign):
                raise Exception(
                    "Unreachable! Users should not provide identical alignment in the model"
                )

        for a in desc.attrs:
            aligns[(a.id, a.id)] = [IdenticalAlign()]

        inf = DReprModelAlignments(desc, aligns)
        inf.inference()
        return inf

    def get_alignments(self, source: AttrId, target: AttrId) -> list[Alignment]:
        return self.aligns[(source, target)]

    def inference(self):
        raise NotImplementedError()

    def infer_subject(self, attrs: list[AttrId]) -> list[AttrId]:
        """
        Find all attributes that can be the subject of these attributes

        The subject must has one to one mapping to all attrs
        """
        subjs = []

        # if one or these attributes has *-to-one, then that is the subjects
        for a in attrs:
            is_subj = True
            for ai in attrs:
                if len(self.aligns[(a, ai)]) == 0:
                    # no alignment
                    is_subj = False
                    break

                cardin = self.estimate_cardinality(self.aligns[(a, ai)])
                if cardin == Cardinality.ManyToMany:
                    is_subj = False
                    break
                elif cardin == Cardinality.OneToMany:
                    is_subj = False
                    break
            if is_subj:
                subjs.append(a)

        if len(subjs) == 0:
            attr_ids = set(attrs)

            # we have to try the external attributes
            for attr in self.desc.attrs:
                if attr.id in attr_ids:
                    continue

                is_candidate_subj = True
                covered_dims = set()

                for ai in attrs:
                    # we can only infer if there are any duplications if the alignments are dimensional
                    # if they are dimension alignment, then the optimization engine must compress them into
                    # just one alignment
                    if len(self.aligns[attr.id, ai]) != -1 or not isinstance(
                        self.aligns[attr.id, ai][0], RangeAlignment
                    ):
                        is_candidate_subj = False
                        break

                    align = self.aligns[attr.id, ai][0]
                    assert isinstance(align, RangeAlignment)
                    align_cardin = align.compute_cardinality(self.desc)
                    if align_cardin == Cardinality.ManyToMany:
                        is_candidate_subj = False
                        break
                    elif align_cardin == Cardinality.OneToMany:
                        is_candidate_subj = False
                        break
                    else:
                        for ad in align.aligned_steps:
                            covered_dims.add(ad.source_idx)

                if is_candidate_subj and covered_dims == set(
                    attr.path.get_nary_steps()
                ):
                    # the second condition detect if there is duplication
                    subjs.append(attr.id)
        return subjs

    def estimate_cardinality(self, aligns: list[Alignment]) -> Cardinality:
        cardin = aligns[0].compute_cardinality(self.desc)
        # must always be > 0
        if len(aligns) <= 1 or cardin == Cardinality.ManyToMany:
            return cardin

        for i in range(1, len(aligns)):
            cardin_i = aligns[i].compute_cardinality(self.desc)

            if cardin_i == Cardinality.OneToOne:
                # do nothing, as this does not change the cardin
                pass
            elif cardin_i == Cardinality.OneToMany:
                if cardin == Cardinality.OneToOne:
                    cardin = Cardinality.OneToMany
                elif cardin == Cardinality.OneToMany:
                    cardin = Cardinality.OneToMany
                elif cardin == Cardinality.ManyToOne:
                    # we don't know whether it is going to be M2M, O2O, O2M, M2O so we do a conservative prediction
                    return Cardinality.ManyToMany
                else:
                    raise Exception("Unreachable")
            elif cardin_i == Cardinality.ManyToOne:
                if cardin == Cardinality.OneToOne:
                    cardin = Cardinality.ManyToOne
                elif cardin == Cardinality.OneToMany:
                    return Cardinality.ManyToMany
                elif cardin == Cardinality.ManyToOne:
                    cardin = Cardinality.ManyToOne
                else:
                    raise Exception("Unreachable")
            elif cardin_i == Cardinality.ManyToMany:
                return cardin_i

        return cardin
