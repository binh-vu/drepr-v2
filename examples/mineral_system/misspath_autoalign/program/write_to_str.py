from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter
from drepr.utils.safe import safe_item_getter
from drepr.utils.safe import safe_len


def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "geokb": "https://geokb.wikibase.cloud/entity/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "xsd": "http://www.w3.org/2001/XMLSchema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "geo": "http://www.opengis.net/ont/geosparql#", "gkbi": "https://geokb.wikibase.cloud/entity/", "gkbp": "https://geokb.wikibase.cloud/wiki/Property/"})
	
	# Transform records of class mndr:EvidenceLayer:2
	pathway_potential_dataset_name_value_0_3 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
	start__local_ast_root__2_6 = 0
	end__local_ast_root__2_7 = safe_len(pathway_potential_dataset_name_value_0_3, "Encounter error while computing number of elements of attribute pathway_potential_dataset_name at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
	for pathway_potential_dataset_name_index_1_4 in range(start__local_ast_root__2_6, end__local_ast_root__2_7):
		pathway_potential_dataset_name_value_1_5 = pathway_potential_dataset_name_value_0_3[pathway_potential_dataset_name_index_1_4]
		pathway_potential_dataset_name_value_2_8 = safe_item_getter(pathway_potential_dataset_name_value_1_5, "pathway", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
		start__local_ast_root__2__8_11 = 0
		end__local_ast_root__2__8_12 = safe_len(pathway_potential_dataset_name_value_2_8, "Encounter error while computing number of elements of attribute pathway_potential_dataset_name at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
		for pathway_potential_dataset_name_index_3_9 in range(start__local_ast_root__2__8_11, end__local_ast_root__2__8_12):
			pathway_potential_dataset_name_value_3_10 = pathway_potential_dataset_name_value_2_8[pathway_potential_dataset_name_index_3_9]
			pathway_potential_dataset_name_value_4_13 = safe_item_getter(pathway_potential_dataset_name_value_3_10, "potential_dataset", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key potential_dataset does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
			start__local_ast_root__2__8__4_16 = 0
			end__local_ast_root__2__8__4_17 = safe_len(pathway_potential_dataset_name_value_4_13, "Encounter error while computing number of elements of attribute pathway_potential_dataset_name at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
			for pathway_potential_dataset_name_index_5_14 in range(start__local_ast_root__2__8__4_16, end__local_ast_root__2__8__4_17):
				pathway_potential_dataset_name_value_5_15 = pathway_potential_dataset_name_value_4_13[pathway_potential_dataset_name_index_5_14]
				pathway_potential_dataset_name_value_6_18 = safe_item_getter(pathway_potential_dataset_name_value_5_15, "name", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key name does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
				writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (4, pathway_potential_dataset_name_index_1_4, pathway_potential_dataset_name_index_3_9, pathway_potential_dataset_name_index_5_14), True, False)
				
				# Retrieve value of data property: pathway_potential_dataset_name
				writer_2.write_data_property("https://minmod.isi.edu/resource/name", pathway_potential_dataset_name_value_6_18, None)
				
				# Retrieve value of data property: pathway_potential_dataset_score
				pathway_potential_dataset_score_value_0_19 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_potential_dataset_score, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score'])")
				pathway_potential_dataset_score_index_1_20 = pathway_potential_dataset_name_index_1_4
				pathway_potential_dataset_score_value_1_21 = safe_item_getter(pathway_potential_dataset_score_value_0_19, pathway_potential_dataset_score_index_1_20, "Encounter error while accessing element of attribute pathway_potential_dataset_score via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score']")
				pathway_potential_dataset_score_value_2_22 = safe_item_getter(pathway_potential_dataset_score_value_1_21, "pathway", "While traveling elements of attribute pathway_potential_dataset_score, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score'])")
				pathway_potential_dataset_score_index_3_23 = pathway_potential_dataset_name_index_3_9
				pathway_potential_dataset_score_value_3_24 = safe_item_getter(pathway_potential_dataset_score_value_2_22, pathway_potential_dataset_score_index_3_23, "Encounter error while accessing element of attribute pathway_potential_dataset_score via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score']")
				pathway_potential_dataset_score_value_4_25 = safe_item_getter(pathway_potential_dataset_score_value_3_24, "potential_dataset", "While traveling elements of attribute pathway_potential_dataset_score, encounter key error: key potential_dataset does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score'])")
				pathway_potential_dataset_score_index_5_26 = pathway_potential_dataset_name_index_5_14
				pathway_potential_dataset_score_value_5_27 = safe_item_getter(pathway_potential_dataset_score_value_4_25, pathway_potential_dataset_score_index_5_26, "Encounter error while accessing element of attribute pathway_potential_dataset_score via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score']")
				pathway_potential_dataset_score_value_6_28 = safe_item_getter(pathway_potential_dataset_score_value_5_27, "relevance_score", "While traveling elements of attribute pathway_potential_dataset_score, encounter key error: key relevance_score does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'relevance_score'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", pathway_potential_dataset_score_value_6_28, None)
				
				writer_2.end_record()
	
	# Transform records of class mndr:Document:2
	pathway_id_document_value_0_29 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_id_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
	start__local_ast_root__2_32 = 0
	end__local_ast_root__2_33 = safe_len(pathway_id_document_value_0_29, "Encounter error while computing number of elements of attribute pathway_id_document at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
	for pathway_id_document_index_1_30 in range(start__local_ast_root__2_32, end__local_ast_root__2_33):
		pathway_id_document_value_1_31 = pathway_id_document_value_0_29[pathway_id_document_index_1_30]
		pathway_id_document_value_2_34 = safe_item_getter(pathway_id_document_value_1_31, "pathway", "While traveling elements of attribute pathway_id_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
		start__local_ast_root__2__14_37 = 0
		end__local_ast_root__2__14_38 = safe_len(pathway_id_document_value_2_34, "Encounter error while computing number of elements of attribute pathway_id_document at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
		for pathway_id_document_index_3_35 in range(start__local_ast_root__2__14_37, end__local_ast_root__2__14_38):
			pathway_id_document_value_3_36 = pathway_id_document_value_2_34[pathway_id_document_index_3_35]
			pathway_id_document_value_4_39 = safe_item_getter(pathway_id_document_value_3_36, "supporting_references", "While traveling elements of attribute pathway_id_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
			start__local_ast_root__2__14__4_42 = 0
			end__local_ast_root__2__14__4_43 = safe_len(pathway_id_document_value_4_39, "Encounter error while computing number of elements of attribute pathway_id_document at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
			for pathway_id_document_index_5_40 in range(start__local_ast_root__2__14__4_42, end__local_ast_root__2__14__4_43):
				pathway_id_document_value_5_41 = pathway_id_document_value_4_39[pathway_id_document_index_5_40]
				pathway_id_document_value_6_44 = safe_item_getter(pathway_id_document_value_5_41, "document", "While traveling elements of attribute pathway_id_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				pathway_id_document_value_7_45 = safe_item_getter(pathway_id_document_value_6_44, "id", "While traveling elements of attribute pathway_id_document, encounter key error: key id does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				writer_2.begin_record("https://minmod.isi.edu/resource/Document", pathway_id_document_value_7_45, False, False)
				
				# Retrieve value of data property: pathway_id_document
				writer_2.write_data_property("https://minmod.isi.edu/resource/id", pathway_id_document_value_7_45, None)
				
				# Retrieve value of data property: pathway_uri_document
				pathway_uri_document_value_0_46 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_uri_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri'])")
				pathway_uri_document_index_1_47 = pathway_id_document_index_1_30
				pathway_uri_document_value_1_48 = safe_item_getter(pathway_uri_document_value_0_46, pathway_uri_document_index_1_47, "Encounter error while accessing element of attribute pathway_uri_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri']")
				pathway_uri_document_value_2_49 = safe_item_getter(pathway_uri_document_value_1_48, "pathway", "While traveling elements of attribute pathway_uri_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri'])")
				pathway_uri_document_index_3_50 = pathway_id_document_index_3_35
				pathway_uri_document_value_3_51 = safe_item_getter(pathway_uri_document_value_2_49, pathway_uri_document_index_3_50, "Encounter error while accessing element of attribute pathway_uri_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri']")
				pathway_uri_document_value_4_52 = safe_item_getter(pathway_uri_document_value_3_51, "supporting_references", "While traveling elements of attribute pathway_uri_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri'])")
				pathway_uri_document_index_5_53 = pathway_id_document_index_5_40
				pathway_uri_document_value_5_54 = safe_item_getter(pathway_uri_document_value_4_52, pathway_uri_document_index_5_53, "Encounter error while accessing element of attribute pathway_uri_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri']")
				pathway_uri_document_value_6_55 = safe_item_getter(pathway_uri_document_value_5_54, "document", "While traveling elements of attribute pathway_uri_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri'])")
				pathway_uri_document_value_7_56 = safe_item_getter(pathway_uri_document_value_6_55, "uri", "While traveling elements of attribute pathway_uri_document, encounter key error: key uri does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'uri'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/uri", pathway_uri_document_value_7_56, None)
				
				# Retrieve value of data property: pathway_doi
				pathway_doi_value_0_57 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_doi, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi'])")
				pathway_doi_index_1_58 = pathway_id_document_index_1_30
				pathway_doi_value_1_59 = safe_item_getter(pathway_doi_value_0_57, pathway_doi_index_1_58, "Encounter error while accessing element of attribute pathway_doi via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi']")
				pathway_doi_value_2_60 = safe_item_getter(pathway_doi_value_1_59, "pathway", "While traveling elements of attribute pathway_doi, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi'])")
				pathway_doi_index_3_61 = pathway_id_document_index_3_35
				pathway_doi_value_3_62 = safe_item_getter(pathway_doi_value_2_60, pathway_doi_index_3_61, "Encounter error while accessing element of attribute pathway_doi via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi']")
				pathway_doi_value_4_63 = safe_item_getter(pathway_doi_value_3_62, "supporting_references", "While traveling elements of attribute pathway_doi, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi'])")
				pathway_doi_index_5_64 = pathway_id_document_index_5_40
				pathway_doi_value_5_65 = safe_item_getter(pathway_doi_value_4_63, pathway_doi_index_5_64, "Encounter error while accessing element of attribute pathway_doi via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi']")
				pathway_doi_value_6_66 = safe_item_getter(pathway_doi_value_5_65, "document", "While traveling elements of attribute pathway_doi, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi'])")
				pathway_doi_value_7_67 = safe_item_getter(pathway_doi_value_6_66, "doi", "While traveling elements of attribute pathway_doi, encounter key error: key doi does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'doi'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/doi", pathway_doi_value_7_67, None)
				
				# Retrieve value of data property: pathway_journal
				pathway_journal_value_0_68 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_journal, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']])")
				pathway_journal_index_1_69 = pathway_id_document_index_1_30
				pathway_journal_value_1_70 = safe_item_getter(pathway_journal_value_0_68, pathway_journal_index_1_69, "Encounter error while accessing element of attribute pathway_journal via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']]")
				pathway_journal_value_2_71 = safe_item_getter(pathway_journal_value_1_70, "pathway", "While traveling elements of attribute pathway_journal, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']])")
				pathway_journal_index_3_72 = pathway_id_document_index_3_35
				pathway_journal_value_3_73 = safe_item_getter(pathway_journal_value_2_71, pathway_journal_index_3_72, "Encounter error while accessing element of attribute pathway_journal via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']]")
				pathway_journal_value_4_74 = safe_item_getter(pathway_journal_value_3_73, "supporting_references", "While traveling elements of attribute pathway_journal, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']])")
				pathway_journal_index_5_75 = pathway_id_document_index_5_40
				pathway_journal_value_5_76 = safe_item_getter(pathway_journal_value_4_74, pathway_journal_index_5_75, "Encounter error while accessing element of attribute pathway_journal via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']]")
				pathway_journal_value_6_77 = safe_item_getter(pathway_journal_value_5_76, "document", "While traveling elements of attribute pathway_journal, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['journal']])")
				if not ("journal") in pathway_journal_value_6_77:
					pass
				else:
					pathway_journal_value_7_78 = pathway_journal_value_6_77["journal"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/journal", pathway_journal_value_7_78, None)
				
				# Retrieve value of data property: pathway_authors
				pathway_authors_value_0_79 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_authors, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors'])")
				pathway_authors_index_1_80 = pathway_id_document_index_1_30
				pathway_authors_value_1_81 = safe_item_getter(pathway_authors_value_0_79, pathway_authors_index_1_80, "Encounter error while accessing element of attribute pathway_authors via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors']")
				pathway_authors_value_2_82 = safe_item_getter(pathway_authors_value_1_81, "pathway", "While traveling elements of attribute pathway_authors, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors'])")
				pathway_authors_index_3_83 = pathway_id_document_index_3_35
				pathway_authors_value_3_84 = safe_item_getter(pathway_authors_value_2_82, pathway_authors_index_3_83, "Encounter error while accessing element of attribute pathway_authors via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors']")
				pathway_authors_value_4_85 = safe_item_getter(pathway_authors_value_3_84, "supporting_references", "While traveling elements of attribute pathway_authors, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors'])")
				pathway_authors_index_5_86 = pathway_id_document_index_5_40
				pathway_authors_value_5_87 = safe_item_getter(pathway_authors_value_4_85, pathway_authors_index_5_86, "Encounter error while accessing element of attribute pathway_authors via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors']")
				pathway_authors_value_6_88 = safe_item_getter(pathway_authors_value_5_87, "document", "While traveling elements of attribute pathway_authors, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors'])")
				pathway_authors_value_7_89 = safe_item_getter(pathway_authors_value_6_88, "authors", "While traveling elements of attribute pathway_authors, encounter key error: key authors does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors'])")
				start__local_ast_root__2__14__4__4_92 = 0
				end__local_ast_root__2__14__4__4_93 = safe_len(pathway_authors_value_7_89, "Encounter error while computing number of elements of attribute pathway_authors at dimension = 8 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'authors']")
				for pathway_authors_index_8_90 in range(start__local_ast_root__2__14__4__4_92, end__local_ast_root__2__14__4__4_93):
					pathway_authors_value_8_91 = pathway_authors_value_7_89[pathway_authors_index_8_90]
					writer_2.write_data_property("https://minmod.isi.edu/resource/authors", pathway_authors_value_8_91, None)
				
				# Retrieve value of data property: pathway_description_document
				pathway_description_document_value_0_94 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_description_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description'])")
				pathway_description_document_index_1_95 = pathway_id_document_index_1_30
				pathway_description_document_value_1_96 = safe_item_getter(pathway_description_document_value_0_94, pathway_description_document_index_1_95, "Encounter error while accessing element of attribute pathway_description_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description']")
				pathway_description_document_value_2_97 = safe_item_getter(pathway_description_document_value_1_96, "pathway", "While traveling elements of attribute pathway_description_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description'])")
				pathway_description_document_index_3_98 = pathway_id_document_index_3_35
				pathway_description_document_value_3_99 = safe_item_getter(pathway_description_document_value_2_97, pathway_description_document_index_3_98, "Encounter error while accessing element of attribute pathway_description_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description']")
				pathway_description_document_value_4_100 = safe_item_getter(pathway_description_document_value_3_99, "supporting_references", "While traveling elements of attribute pathway_description_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description'])")
				pathway_description_document_index_5_101 = pathway_id_document_index_5_40
				pathway_description_document_value_5_102 = safe_item_getter(pathway_description_document_value_4_100, pathway_description_document_index_5_101, "Encounter error while accessing element of attribute pathway_description_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description']")
				pathway_description_document_value_6_103 = safe_item_getter(pathway_description_document_value_5_102, "document", "While traveling elements of attribute pathway_description_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description'])")
				pathway_description_document_value_7_104 = safe_item_getter(pathway_description_document_value_6_103, "description", "While traveling elements of attribute pathway_description_document, encounter key error: key description does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'description'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/description", pathway_description_document_value_7_104, None)
				
				# Retrieve value of data property: pathway_title_document
				pathway_title_document_value_0_105 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_title_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title'])")
				pathway_title_document_index_1_106 = pathway_id_document_index_1_30
				pathway_title_document_value_1_107 = safe_item_getter(pathway_title_document_value_0_105, pathway_title_document_index_1_106, "Encounter error while accessing element of attribute pathway_title_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title']")
				pathway_title_document_value_2_108 = safe_item_getter(pathway_title_document_value_1_107, "pathway", "While traveling elements of attribute pathway_title_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title'])")
				pathway_title_document_index_3_109 = pathway_id_document_index_3_35
				pathway_title_document_value_3_110 = safe_item_getter(pathway_title_document_value_2_108, pathway_title_document_index_3_109, "Encounter error while accessing element of attribute pathway_title_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title']")
				pathway_title_document_value_4_111 = safe_item_getter(pathway_title_document_value_3_110, "supporting_references", "While traveling elements of attribute pathway_title_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title'])")
				pathway_title_document_index_5_112 = pathway_id_document_index_5_40
				pathway_title_document_value_5_113 = safe_item_getter(pathway_title_document_value_4_111, pathway_title_document_index_5_112, "Encounter error while accessing element of attribute pathway_title_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title']")
				pathway_title_document_value_6_114 = safe_item_getter(pathway_title_document_value_5_113, "document", "While traveling elements of attribute pathway_title_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title'])")
				pathway_title_document_value_7_115 = safe_item_getter(pathway_title_document_value_6_114, "title", "While traveling elements of attribute pathway_title_document, encounter key error: key title does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'title'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/title", pathway_title_document_value_7_115, None)
				
				# Retrieve value of data property: pathway_volume
				pathway_volume_value_0_116 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_volume, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']])")
				pathway_volume_index_1_117 = pathway_id_document_index_1_30
				pathway_volume_value_1_118 = safe_item_getter(pathway_volume_value_0_116, pathway_volume_index_1_117, "Encounter error while accessing element of attribute pathway_volume via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']]")
				pathway_volume_value_2_119 = safe_item_getter(pathway_volume_value_1_118, "pathway", "While traveling elements of attribute pathway_volume, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']])")
				pathway_volume_index_3_120 = pathway_id_document_index_3_35
				pathway_volume_value_3_121 = safe_item_getter(pathway_volume_value_2_119, pathway_volume_index_3_120, "Encounter error while accessing element of attribute pathway_volume via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']]")
				pathway_volume_value_4_122 = safe_item_getter(pathway_volume_value_3_121, "supporting_references", "While traveling elements of attribute pathway_volume, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']])")
				pathway_volume_index_5_123 = pathway_id_document_index_5_40
				pathway_volume_value_5_124 = safe_item_getter(pathway_volume_value_4_122, pathway_volume_index_5_123, "Encounter error while accessing element of attribute pathway_volume via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']]")
				pathway_volume_value_6_125 = safe_item_getter(pathway_volume_value_5_124, "document", "While traveling elements of attribute pathway_volume, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['volume']])")
				if not ("volume") in pathway_volume_value_6_125:
					pass
				else:
					pathway_volume_value_7_126 = pathway_volume_value_6_125["volume"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/volume", pathway_volume_value_7_126, None)
				
				# Retrieve value of data property: pathway_issue_document
				pathway_issue_document_value_0_127 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_issue_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']])")
				pathway_issue_document_index_1_128 = pathway_id_document_index_1_30
				pathway_issue_document_value_1_129 = safe_item_getter(pathway_issue_document_value_0_127, pathway_issue_document_index_1_128, "Encounter error while accessing element of attribute pathway_issue_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']]")
				pathway_issue_document_value_2_130 = safe_item_getter(pathway_issue_document_value_1_129, "pathway", "While traveling elements of attribute pathway_issue_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']])")
				pathway_issue_document_index_3_131 = pathway_id_document_index_3_35
				pathway_issue_document_value_3_132 = safe_item_getter(pathway_issue_document_value_2_130, pathway_issue_document_index_3_131, "Encounter error while accessing element of attribute pathway_issue_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']]")
				pathway_issue_document_value_4_133 = safe_item_getter(pathway_issue_document_value_3_132, "supporting_references", "While traveling elements of attribute pathway_issue_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']])")
				pathway_issue_document_index_5_134 = pathway_id_document_index_5_40
				pathway_issue_document_value_5_135 = safe_item_getter(pathway_issue_document_value_4_133, pathway_issue_document_index_5_134, "Encounter error while accessing element of attribute pathway_issue_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']]")
				pathway_issue_document_value_6_136 = safe_item_getter(pathway_issue_document_value_5_135, "document", "While traveling elements of attribute pathway_issue_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', ['issue']])")
				if not ("issue") in pathway_issue_document_value_6_136:
					pass
				else:
					pathway_issue_document_value_7_137 = pathway_issue_document_value_6_136["issue"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/issue", pathway_issue_document_value_7_137, None)
				
				# Retrieve value of data property: pathway_month_document
				pathway_month_document_value_0_138 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_month_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month'])")
				pathway_month_document_index_1_139 = pathway_id_document_index_1_30
				pathway_month_document_value_1_140 = safe_item_getter(pathway_month_document_value_0_138, pathway_month_document_index_1_139, "Encounter error while accessing element of attribute pathway_month_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month']")
				pathway_month_document_value_2_141 = safe_item_getter(pathway_month_document_value_1_140, "pathway", "While traveling elements of attribute pathway_month_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month'])")
				pathway_month_document_index_3_142 = pathway_id_document_index_3_35
				pathway_month_document_value_3_143 = safe_item_getter(pathway_month_document_value_2_141, pathway_month_document_index_3_142, "Encounter error while accessing element of attribute pathway_month_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month']")
				pathway_month_document_value_4_144 = safe_item_getter(pathway_month_document_value_3_143, "supporting_references", "While traveling elements of attribute pathway_month_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month'])")
				pathway_month_document_index_5_145 = pathway_id_document_index_5_40
				pathway_month_document_value_5_146 = safe_item_getter(pathway_month_document_value_4_144, pathway_month_document_index_5_145, "Encounter error while accessing element of attribute pathway_month_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month']")
				pathway_month_document_value_6_147 = safe_item_getter(pathway_month_document_value_5_146, "document", "While traveling elements of attribute pathway_month_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month'])")
				pathway_month_document_value_7_148 = safe_item_getter(pathway_month_document_value_6_147, "month", "While traveling elements of attribute pathway_month_document, encounter key error: key month does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'month'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/month", pathway_month_document_value_7_148, None)
				
				# Retrieve value of data property: pathway_year_document
				pathway_year_document_value_0_149 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_year_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year'])")
				pathway_year_document_index_1_150 = pathway_id_document_index_1_30
				pathway_year_document_value_1_151 = safe_item_getter(pathway_year_document_value_0_149, pathway_year_document_index_1_150, "Encounter error while accessing element of attribute pathway_year_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year']")
				pathway_year_document_value_2_152 = safe_item_getter(pathway_year_document_value_1_151, "pathway", "While traveling elements of attribute pathway_year_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year'])")
				pathway_year_document_index_3_153 = pathway_id_document_index_3_35
				pathway_year_document_value_3_154 = safe_item_getter(pathway_year_document_value_2_152, pathway_year_document_index_3_153, "Encounter error while accessing element of attribute pathway_year_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year']")
				pathway_year_document_value_4_155 = safe_item_getter(pathway_year_document_value_3_154, "supporting_references", "While traveling elements of attribute pathway_year_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year'])")
				pathway_year_document_index_5_156 = pathway_id_document_index_5_40
				pathway_year_document_value_5_157 = safe_item_getter(pathway_year_document_value_4_155, pathway_year_document_index_5_156, "Encounter error while accessing element of attribute pathway_year_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year']")
				pathway_year_document_value_6_158 = safe_item_getter(pathway_year_document_value_5_157, "document", "While traveling elements of attribute pathway_year_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year'])")
				pathway_year_document_value_7_159 = safe_item_getter(pathway_year_document_value_6_158, "year", "While traveling elements of attribute pathway_year_document, encounter key error: key year does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'year'])")
				writer_2.write_data_property("https://minmod.isi.edu/resource/year", pathway_year_document_value_7_159, None)
				
				writer_2.end_record()
	
	# Transform records of class mndr:Reference:2
	pathway_id_reference_value_0_160 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_id_reference, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
	start__local_ast_root__2_163 = 0
	end__local_ast_root__2_164 = safe_len(pathway_id_reference_value_0_160, "Encounter error while computing number of elements of attribute pathway_id_reference at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
	for pathway_id_reference_index_1_161 in range(start__local_ast_root__2_163, end__local_ast_root__2_164):
		pathway_id_reference_value_1_162 = pathway_id_reference_value_0_160[pathway_id_reference_index_1_161]
		pathway_id_reference_value_2_165 = safe_item_getter(pathway_id_reference_value_1_162, "pathway", "While traveling elements of attribute pathway_id_reference, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
		start__local_ast_root__2__20_168 = 0
		end__local_ast_root__2__20_169 = safe_len(pathway_id_reference_value_2_165, "Encounter error while computing number of elements of attribute pathway_id_reference at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
		for pathway_id_reference_index_3_166 in range(start__local_ast_root__2__20_168, end__local_ast_root__2__20_169):
			pathway_id_reference_value_3_167 = pathway_id_reference_value_2_165[pathway_id_reference_index_3_166]
			pathway_id_reference_value_4_170 = safe_item_getter(pathway_id_reference_value_3_167, "supporting_references", "While traveling elements of attribute pathway_id_reference, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
			start__local_ast_root__2__20__4_173 = 0
			end__local_ast_root__2__20__4_174 = safe_len(pathway_id_reference_value_4_170, "Encounter error while computing number of elements of attribute pathway_id_reference at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
			for pathway_id_reference_index_5_171 in range(start__local_ast_root__2__20__4_173, end__local_ast_root__2__20__4_174):
				pathway_id_reference_value_5_172 = pathway_id_reference_value_4_170[pathway_id_reference_index_5_171]
				pathway_id_reference_value_6_175 = safe_item_getter(pathway_id_reference_value_5_172, "id", "While traveling elements of attribute pathway_id_reference, encounter key error: key id does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
				writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (6, pathway_id_reference_index_1_161, pathway_id_reference_index_3_166, pathway_id_reference_index_5_171), True, False)
				
				# Retrieve value of data property: pathway_id_reference
				writer_2.write_data_property("https://minmod.isi.edu/resource/date", pathway_id_reference_value_6_175, None)
				
				# Retrieve value of object property: pathway_id_document
				pathway_id_document_value_0_176 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_id_document, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				pathway_id_document_index_1_177 = pathway_id_reference_index_1_161
				pathway_id_document_value_1_178 = safe_item_getter(pathway_id_document_value_0_176, pathway_id_document_index_1_177, "Encounter error while accessing element of attribute pathway_id_document via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
				pathway_id_document_value_2_179 = safe_item_getter(pathway_id_document_value_1_178, "pathway", "While traveling elements of attribute pathway_id_document, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				pathway_id_document_index_3_180 = pathway_id_reference_index_3_166
				pathway_id_document_value_3_181 = safe_item_getter(pathway_id_document_value_2_179, pathway_id_document_index_3_180, "Encounter error while accessing element of attribute pathway_id_document via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
				pathway_id_document_value_4_182 = safe_item_getter(pathway_id_document_value_3_181, "supporting_references", "While traveling elements of attribute pathway_id_document, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				pathway_id_document_index_5_183 = pathway_id_reference_index_5_171
				pathway_id_document_value_5_184 = safe_item_getter(pathway_id_document_value_4_182, pathway_id_document_index_5_183, "Encounter error while accessing element of attribute pathway_id_document via alignment at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id']")
				pathway_id_document_value_6_185 = safe_item_getter(pathway_id_document_value_5_184, "document", "While traveling elements of attribute pathway_id_document, encounter key error: key document does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				pathway_id_document_value_7_186 = safe_item_getter(pathway_id_document_value_6_185, "id", "While traveling elements of attribute pathway_id_document, encounter key error: key id does not exist (key position = 7 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'document', 'id'])")
				writer_2.write_object_property("https://minmod.isi.edu/resource/document", pathway_id_document_value_7_186, True, False, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:2
	pathway_criteria_value_0_187 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_criteria, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
	start__local_ast_root__2_190 = 0
	end__local_ast_root__2_191 = safe_len(pathway_criteria_value_0_187, "Encounter error while computing number of elements of attribute pathway_criteria at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria']")
	for pathway_criteria_index_1_188 in range(start__local_ast_root__2_190, end__local_ast_root__2_191):
		pathway_criteria_value_1_189 = pathway_criteria_value_0_187[pathway_criteria_index_1_188]
		pathway_criteria_value_2_192 = safe_item_getter(pathway_criteria_value_1_189, "pathway", "While traveling elements of attribute pathway_criteria, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
		start__local_ast_root__2__26_195 = 0
		end__local_ast_root__2__26_196 = safe_len(pathway_criteria_value_2_192, "Encounter error while computing number of elements of attribute pathway_criteria at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria']")
		for pathway_criteria_index_3_193 in range(start__local_ast_root__2__26_195, end__local_ast_root__2__26_196):
			pathway_criteria_value_3_194 = pathway_criteria_value_2_192[pathway_criteria_index_3_193]
			pathway_criteria_value_4_197 = safe_item_getter(pathway_criteria_value_3_194, "criteria", "While traveling elements of attribute pathway_criteria, encounter key error: key criteria does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
			writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (2, pathway_criteria_index_1_188, pathway_criteria_index_3_193), True, False)
			
			# Retrieve value of data property: pathway_criteria
			writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", pathway_criteria_value_4_197, None)
			
			# Retrieve value of data property: pathway_theorectical
			pathway_theorectical_value_0_198 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_theorectical, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'theorectical'])")
			pathway_theorectical_index_1_199 = pathway_criteria_index_1_188
			pathway_theorectical_value_1_200 = safe_item_getter(pathway_theorectical_value_0_198, pathway_theorectical_index_1_199, "Encounter error while accessing element of attribute pathway_theorectical via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'theorectical']")
			pathway_theorectical_value_2_201 = safe_item_getter(pathway_theorectical_value_1_200, "pathway", "While traveling elements of attribute pathway_theorectical, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'theorectical'])")
			pathway_theorectical_index_3_202 = pathway_criteria_index_3_193
			pathway_theorectical_value_3_203 = safe_item_getter(pathway_theorectical_value_2_201, pathway_theorectical_index_3_202, "Encounter error while accessing element of attribute pathway_theorectical via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'theorectical']")
			pathway_theorectical_value_4_204 = safe_item_getter(pathway_theorectical_value_3_203, "theorectical", "While traveling elements of attribute pathway_theorectical, encounter key error: key theorectical does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'theorectical'])")
			writer_2.write_data_property("https://minmod.isi.edu/resource/theorectical", pathway_theorectical_value_4_204, None)
			
			# Retrieve value of object property: pathway_potential_dataset_name
			pathway_potential_dataset_name_value_0_205 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
			pathway_potential_dataset_name_index_1_206 = pathway_criteria_index_1_188
			pathway_potential_dataset_name_value_1_207 = safe_item_getter(pathway_potential_dataset_name_value_0_205, pathway_potential_dataset_name_index_1_206, "Encounter error while accessing element of attribute pathway_potential_dataset_name via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
			pathway_potential_dataset_name_value_2_208 = safe_item_getter(pathway_potential_dataset_name_value_1_207, "pathway", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
			pathway_potential_dataset_name_index_3_209 = pathway_criteria_index_3_193
			pathway_potential_dataset_name_value_3_210 = safe_item_getter(pathway_potential_dataset_name_value_2_208, pathway_potential_dataset_name_index_3_209, "Encounter error while accessing element of attribute pathway_potential_dataset_name via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
			pathway_potential_dataset_name_value_4_211 = safe_item_getter(pathway_potential_dataset_name_value_3_210, "potential_dataset", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key potential_dataset does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
			start__local_ast_root__2__26__4_214 = 0
			end__local_ast_root__2__26__4_215 = safe_len(pathway_potential_dataset_name_value_4_211, "Encounter error while computing number of elements of attribute pathway_potential_dataset_name at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name']")
			for pathway_potential_dataset_name_index_5_212 in range(start__local_ast_root__2__26__4_214, end__local_ast_root__2__26__4_215):
				pathway_potential_dataset_name_value_5_213 = pathway_potential_dataset_name_value_4_211[pathway_potential_dataset_name_index_5_212]
				pathway_potential_dataset_name_value_6_216 = safe_item_getter(pathway_potential_dataset_name_value_5_213, "name", "While traveling elements of attribute pathway_potential_dataset_name, encounter key error: key name does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'potential_dataset', '0..:1', 'name'])")
				writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (4, pathway_potential_dataset_name_index_1_206, pathway_potential_dataset_name_index_3_209, pathway_potential_dataset_name_index_5_212), True, True, False)
			
			# Retrieve value of object property: pathway_id_reference
			pathway_id_reference_value_0_217 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_id_reference, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
			pathway_id_reference_index_1_218 = pathway_criteria_index_1_188
			pathway_id_reference_value_1_219 = safe_item_getter(pathway_id_reference_value_0_217, pathway_id_reference_index_1_218, "Encounter error while accessing element of attribute pathway_id_reference via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
			pathway_id_reference_value_2_220 = safe_item_getter(pathway_id_reference_value_1_219, "pathway", "While traveling elements of attribute pathway_id_reference, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
			pathway_id_reference_index_3_221 = pathway_criteria_index_3_193
			pathway_id_reference_value_3_222 = safe_item_getter(pathway_id_reference_value_2_220, pathway_id_reference_index_3_221, "Encounter error while accessing element of attribute pathway_id_reference via alignment at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
			pathway_id_reference_value_4_223 = safe_item_getter(pathway_id_reference_value_3_222, "supporting_references", "While traveling elements of attribute pathway_id_reference, encounter key error: key supporting_references does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
			start__local_ast_root__2__26__4_226 = 0
			end__local_ast_root__2__26__4_227 = safe_len(pathway_id_reference_value_4_223, "Encounter error while computing number of elements of attribute pathway_id_reference at dimension = 5 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id']")
			for pathway_id_reference_index_5_224 in range(start__local_ast_root__2__26__4_226, end__local_ast_root__2__26__4_227):
				pathway_id_reference_value_5_225 = pathway_id_reference_value_4_223[pathway_id_reference_index_5_224]
				pathway_id_reference_value_6_228 = safe_item_getter(pathway_id_reference_value_5_225, "id", "While traveling elements of attribute pathway_id_reference, encounter key error: key id does not exist (key position = 6 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'supporting_references', '0..:1', 'id'])")
				writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (6, pathway_id_reference_index_1_218, pathway_id_reference_index_3_221, pathway_id_reference_index_5_224), True, True, False)
			
			writer_2.end_record()
	
	# Transform records of class mndr:MineralSystem:1
	ms_id_value_0_229 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute ms_id, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'id'])")
	start__local_ast_root__2_232 = 0
	end__local_ast_root__2_233 = safe_len(ms_id_value_0_229, "Encounter error while computing number of elements of attribute ms_id at dimension = 1 - full path = ['MineralSystem', '0..:1', 'id']")
	for ms_id_index_1_230 in range(start__local_ast_root__2_232, end__local_ast_root__2_233):
		ms_id_value_1_231 = ms_id_value_0_229[ms_id_index_1_230]
		ms_id_value_2_234 = safe_item_getter(ms_id_value_1_231, "id", "While traveling elements of attribute ms_id, encounter key error: key id does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'id'])")
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSystem", (0, ms_id_index_1_230), True, False)
		
		# Retrieve value of data property: ms_id
		writer_2.write_data_property("https://minmod.isi.edu/resource/id", ms_id_value_2_234, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_value_0_235 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute deposit_type, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'deposit_type', '0..:1'])")
		deposit_type_index_1_236 = ms_id_index_1_230
		deposit_type_value_1_237 = safe_item_getter(deposit_type_value_0_235, deposit_type_index_1_236, "Encounter error while accessing element of attribute deposit_type via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'deposit_type', '0..:1']")
		deposit_type_value_2_238 = safe_item_getter(deposit_type_value_1_237, "deposit_type", "While traveling elements of attribute deposit_type, encounter key error: key deposit_type does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'deposit_type', '0..:1'])")
		start__local_ast_root__2__32_241 = 0
		end__local_ast_root__2__32_242 = safe_len(deposit_type_value_2_238, "Encounter error while computing number of elements of attribute deposit_type at dimension = 3 - full path = ['MineralSystem', '0..:1', 'deposit_type', '0..:1']")
		for deposit_type_index_3_239 in range(start__local_ast_root__2__32_241, end__local_ast_root__2__32_242):
			deposit_type_value_3_240 = deposit_type_value_2_238[deposit_type_index_3_239]
			writer_2.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_3_240, "drepr:uri")
		
		# Retrieve value of object property: pathway_criteria
		pathway_criteria_value_0_243 = safe_item_getter(resource_data_1, "MineralSystem", "While traveling elements of attribute pathway_criteria, encounter key error: key MineralSystem does not exist (key position = 0 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
		pathway_criteria_index_1_244 = ms_id_index_1_230
		pathway_criteria_value_1_245 = safe_item_getter(pathway_criteria_value_0_243, pathway_criteria_index_1_244, "Encounter error while accessing element of attribute pathway_criteria via alignment at dimension = 1 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria']")
		pathway_criteria_value_2_246 = safe_item_getter(pathway_criteria_value_1_245, "pathway", "While traveling elements of attribute pathway_criteria, encounter key error: key pathway does not exist (key position = 2 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
		start__local_ast_root__2__32_249 = 0
		end__local_ast_root__2__32_250 = safe_len(pathway_criteria_value_2_246, "Encounter error while computing number of elements of attribute pathway_criteria at dimension = 3 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria']")
		for pathway_criteria_index_3_247 in range(start__local_ast_root__2__32_249, end__local_ast_root__2__32_250):
			pathway_criteria_value_3_248 = pathway_criteria_value_2_246[pathway_criteria_index_3_247]
			pathway_criteria_value_4_251 = safe_item_getter(pathway_criteria_value_3_248, "criteria", "While traveling elements of attribute pathway_criteria, encounter key error: key criteria does not exist (key position = 4 - full path = ['MineralSystem', '0..:1', 'pathway', '0..:1', 'criteria'])")
			writer_2.write_object_property("https://minmod.isi.edu/resource/pathway", (2, pathway_criteria_index_1_244, pathway_criteria_index_3_247), True, True, False)
		
		writer_2.end_record()
	
	output_252 = writer_2.write_to_string()
	return output_252

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))