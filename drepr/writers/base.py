from __future__ import annotations

from typing import Any


class StreamClassWriter:

    def has_written_record(self, class_id: str, subject: str) -> bool:
        """Test if a record of a given class `class_id` has been written"""
        ...

    def begin_record(self, subject: str, is_blank: bool) -> bool:
        """
        Tell the writer that we are going to write a record, and we already have all information of the
        record to write.
        The function return `true` if this is a new record, otherwise `false`.

        # Arguments

        * `subject` - real id of the record, which is determined by the value of `drepr:uri` property
                                of the record or generated randomly (if it's a blank node)
        * `is_blank` - whether this subject is a blank node or not
        """
        ...

    def end_record(self):
        """
        Tell the writer that we finish writing all information of the record. This method cannot be
        called before `begin_record` method.

        Note: this method should not be called if the function `begin_record` return `false`
        """
        ...

    def begin_partial_buffering_record(self, subject: str, is_blank: bool) -> bool:
        """
        Tell the writer that we are going to write a record, and we don't have some information about
        the links between the records and other records as the other records haven't been generated
        yet.
        The function return `true` if this is a new record, otherwise `false`.

        # Arguments

        * `subject` - real id of the record, which is determined by the value of `drepr:uri` property
                                of the record
        * `is_blank` - whether this subject is a blank node or not
        """
        ...

    def write_data_property(self, subject: str, predicate_id: str, value: Any):
        """
        Write value of a data property of the current record.

        # Arguments

        * `subject` - real id of the current record
        * `predicate_id` - id of the data property that we are writing to (`edge_id` of the edge in the
                        semantic model)
        * `value` - value of the property
        """

    def write_object_property(
        self,
        predicate_id: str,
        object: str,
        is_subject_blank: bool,
        is_object_blank: bool,
        is_new_subj: bool,
    ):
        """
        Write value of a object property of the current record.

        # Arguments

        * `predicate_id` - id of the object property that we are writing to (`edge_id` of the edge in the
                        semantic model)
        * `object` - id of the target record
        * `is_subject_blank` - whether the subject id is blank
        * `is_object_blank` - whether the object id is blank
        * `is_new_subj` - whether the current record is a new record or an existing record (obtained
                          from the `begin_record` or `begin_partial_buffering_record` function
        """
        ...

    def buffer_object_property(
        self,
        target_cls: str,
        predicate_id: str,
        object: str,
        is_object_blank: bool,
    ):
        """
        Write value of a object property of the current record into buffer because we haven't generated
        the target object, it may be missed later.

        # Arguments

        * `target_cls`: id of the class of the target record that the current record is linked to,
                        which is the `node_id` of the class node in the semantic model
        * `predicate_id` - id of the object property that we are writing to (`edge_id` of the edge in the
                        semantic model)
        * `object` - id of the target record
        * `is_object_blank` - whether the object is blank node or not
        """
