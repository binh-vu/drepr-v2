from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0, output_file_1):
	resource_data_2 = read_source_json(resource_0)
	
	writer_3 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "geokb": "https://geokb.wikibase.cloud/entity/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "xsd": "http://www.w3.org/2001/XMLSchema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "geo": "http://www.opengis.net/ont/geosparql#", "gkbi": "https://geokb.wikibase.cloud/entity/", "gkbp": "https://geokb.wikibase.cloud/wiki/Property/"})
	
	# Transform records of class mndr:EvidenceLayer:2
	pathway_potential_dataset_name_value_0_4 = resource_data_2["MineralSystem"]
	start_5 = 0
	end_6 = len(pathway_potential_dataset_name_value_0_4)
	for pathway_potential_dataset_name_index_1_7 in range(start_5, end_6):
		pathway_potential_dataset_name_value_1_8 = pathway_potential_dataset_name_value_0_4[pathway_potential_dataset_name_index_1_7]
		pathway_potential_dataset_name_value_2_9 = pathway_potential_dataset_name_value_1_8["pathway"]
		start_10 = 0
		end_11 = len(pathway_potential_dataset_name_value_2_9)
		for pathway_potential_dataset_name_index_3_12 in range(start_10, end_11):
			pathway_potential_dataset_name_value_3_13 = pathway_potential_dataset_name_value_2_9[pathway_potential_dataset_name_index_3_12]
			pathway_potential_dataset_name_value_4_14 = pathway_potential_dataset_name_value_3_13["potential_dataset"]
			start_15 = 0
			end_16 = len(pathway_potential_dataset_name_value_4_14)
			for pathway_potential_dataset_name_index_5_17 in range(start_15, end_16):
				pathway_potential_dataset_name_value_5_18 = pathway_potential_dataset_name_value_4_14[pathway_potential_dataset_name_index_5_17]
				pathway_potential_dataset_name_value_6_19 = pathway_potential_dataset_name_value_5_18["name"]
				writer_3.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (4, pathway_potential_dataset_name_index_1_7, pathway_potential_dataset_name_index_3_12, pathway_potential_dataset_name_index_5_17), True, False)
				
				# Retrieve value of data property: pathway_potential_dataset_name
				writer_3.write_data_property("https://minmod.isi.edu/resource/name", pathway_potential_dataset_name_value_6_19, None)
				
				# Retrieve value of data property: pathway_potential_dataset_score
				pathway_potential_dataset_score_value_0_20 = resource_data_2["MineralSystem"]
				pathway_potential_dataset_score_index_1_21 = pathway_potential_dataset_name_index_1_7
				pathway_potential_dataset_score_value_1_22 = pathway_potential_dataset_score_value_0_20[pathway_potential_dataset_score_index_1_21]
				pathway_potential_dataset_score_value_2_23 = pathway_potential_dataset_score_value_1_22["pathway"]
				pathway_potential_dataset_score_index_3_24 = pathway_potential_dataset_name_index_3_12
				pathway_potential_dataset_score_value_3_25 = pathway_potential_dataset_score_value_2_23[pathway_potential_dataset_score_index_3_24]
				pathway_potential_dataset_score_value_4_26 = pathway_potential_dataset_score_value_3_25["potential_dataset"]
				pathway_potential_dataset_score_index_5_27 = pathway_potential_dataset_name_index_5_17
				pathway_potential_dataset_score_value_5_28 = pathway_potential_dataset_score_value_4_26[pathway_potential_dataset_score_index_5_27]
				pathway_potential_dataset_score_value_6_29 = pathway_potential_dataset_score_value_5_28["relevance_score"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/evidence_score", pathway_potential_dataset_score_value_6_29, None)
				
				writer_3.end_record()
	
	# Transform records of class mndr:Document:2
	pathway_id_document_value_0_30 = resource_data_2["MineralSystem"]
	start_31 = 0
	end_32 = len(pathway_id_document_value_0_30)
	for pathway_id_document_index_1_33 in range(start_31, end_32):
		pathway_id_document_value_1_34 = pathway_id_document_value_0_30[pathway_id_document_index_1_33]
		pathway_id_document_value_2_35 = pathway_id_document_value_1_34["pathway"]
		start_36 = 0
		end_37 = len(pathway_id_document_value_2_35)
		for pathway_id_document_index_3_38 in range(start_36, end_37):
			pathway_id_document_value_3_39 = pathway_id_document_value_2_35[pathway_id_document_index_3_38]
			pathway_id_document_value_4_40 = pathway_id_document_value_3_39["supporting_references"]
			start_41 = 0
			end_42 = len(pathway_id_document_value_4_40)
			for pathway_id_document_index_5_43 in range(start_41, end_42):
				pathway_id_document_value_5_44 = pathway_id_document_value_4_40[pathway_id_document_index_5_43]
				pathway_id_document_value_6_45 = pathway_id_document_value_5_44["document"]
				pathway_id_document_value_7_46 = pathway_id_document_value_6_45["id"]
				writer_3.begin_record("https://minmod.isi.edu/resource/Document", pathway_id_document_value_7_46, False, False)
				
				# Retrieve value of data property: pathway_id_document
				writer_3.write_data_property("https://minmod.isi.edu/resource/id", pathway_id_document_value_7_46, None)
				
				# Retrieve value of data property: pathway_uri_document
				pathway_uri_document_value_0_47 = resource_data_2["MineralSystem"]
				pathway_uri_document_index_1_48 = pathway_id_document_index_1_33
				pathway_uri_document_value_1_49 = pathway_uri_document_value_0_47[pathway_uri_document_index_1_48]
				pathway_uri_document_value_2_50 = pathway_uri_document_value_1_49["pathway"]
				pathway_uri_document_index_3_51 = pathway_id_document_index_3_38
				pathway_uri_document_value_3_52 = pathway_uri_document_value_2_50[pathway_uri_document_index_3_51]
				pathway_uri_document_value_4_53 = pathway_uri_document_value_3_52["supporting_references"]
				pathway_uri_document_index_5_54 = pathway_id_document_index_5_43
				pathway_uri_document_value_5_55 = pathway_uri_document_value_4_53[pathway_uri_document_index_5_54]
				pathway_uri_document_value_6_56 = pathway_uri_document_value_5_55["document"]
				pathway_uri_document_value_7_57 = pathway_uri_document_value_6_56["uri"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/uri", pathway_uri_document_value_7_57, None)
				
				# Retrieve value of data property: pathway_doi
				pathway_doi_value_0_58 = resource_data_2["MineralSystem"]
				pathway_doi_index_1_59 = pathway_id_document_index_1_33
				pathway_doi_value_1_60 = pathway_doi_value_0_58[pathway_doi_index_1_59]
				pathway_doi_value_2_61 = pathway_doi_value_1_60["pathway"]
				pathway_doi_index_3_62 = pathway_id_document_index_3_38
				pathway_doi_value_3_63 = pathway_doi_value_2_61[pathway_doi_index_3_62]
				pathway_doi_value_4_64 = pathway_doi_value_3_63["supporting_references"]
				pathway_doi_index_5_65 = pathway_id_document_index_5_43
				pathway_doi_value_5_66 = pathway_doi_value_4_64[pathway_doi_index_5_65]
				pathway_doi_value_6_67 = pathway_doi_value_5_66["document"]
				pathway_doi_value_7_68 = pathway_doi_value_6_67["doi"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/doi", pathway_doi_value_7_68, None)
				
				# Retrieve value of data property: pathway_journal
				pathway_journal_value_0_69 = resource_data_2["MineralSystem"]
				pathway_journal_index_1_70 = pathway_id_document_index_1_33
				pathway_journal_value_1_71 = pathway_journal_value_0_69[pathway_journal_index_1_70]
				pathway_journal_value_2_72 = pathway_journal_value_1_71["pathway"]
				pathway_journal_index_3_73 = pathway_id_document_index_3_38
				pathway_journal_value_3_74 = pathway_journal_value_2_72[pathway_journal_index_3_73]
				pathway_journal_value_4_75 = pathway_journal_value_3_74["supporting_references"]
				pathway_journal_index_5_76 = pathway_id_document_index_5_43
				pathway_journal_value_5_77 = pathway_journal_value_4_75[pathway_journal_index_5_76]
				pathway_journal_value_6_78 = pathway_journal_value_5_77["document"]
				if not ("journal" in pathway_journal_value_6_78):
					pass
				else:
					pathway_journal_value_7_79 = pathway_journal_value_6_78["journal"]
					if True:
						writer_3.write_data_property("https://minmod.isi.edu/resource/journal", pathway_journal_value_7_79, None)
				
				# Retrieve value of data property: pathway_authors
				pathway_authors_value_0_80 = resource_data_2["MineralSystem"]
				pathway_authors_index_1_81 = pathway_id_document_index_1_33
				pathway_authors_value_1_82 = pathway_authors_value_0_80[pathway_authors_index_1_81]
				pathway_authors_value_2_83 = pathway_authors_value_1_82["pathway"]
				pathway_authors_index_3_84 = pathway_id_document_index_3_38
				pathway_authors_value_3_85 = pathway_authors_value_2_83[pathway_authors_index_3_84]
				pathway_authors_value_4_86 = pathway_authors_value_3_85["supporting_references"]
				pathway_authors_index_5_87 = pathway_id_document_index_5_43
				pathway_authors_value_5_88 = pathway_authors_value_4_86[pathway_authors_index_5_87]
				pathway_authors_value_6_89 = pathway_authors_value_5_88["document"]
				pathway_authors_value_7_90 = pathway_authors_value_6_89["authors"]
				start_91 = 0
				end_92 = len(pathway_authors_value_7_90)
				for pathway_authors_index_8_93 in range(start_91, end_92):
					pathway_authors_value_8_94 = pathway_authors_value_7_90[pathway_authors_index_8_93]
					writer_3.write_data_property("https://minmod.isi.edu/resource/authors", pathway_authors_value_8_94, None)
				
				# Retrieve value of data property: pathway_description_document
				pathway_description_document_value_0_95 = resource_data_2["MineralSystem"]
				pathway_description_document_index_1_96 = pathway_id_document_index_1_33
				pathway_description_document_value_1_97 = pathway_description_document_value_0_95[pathway_description_document_index_1_96]
				pathway_description_document_value_2_98 = pathway_description_document_value_1_97["pathway"]
				pathway_description_document_index_3_99 = pathway_id_document_index_3_38
				pathway_description_document_value_3_100 = pathway_description_document_value_2_98[pathway_description_document_index_3_99]
				pathway_description_document_value_4_101 = pathway_description_document_value_3_100["supporting_references"]
				pathway_description_document_index_5_102 = pathway_id_document_index_5_43
				pathway_description_document_value_5_103 = pathway_description_document_value_4_101[pathway_description_document_index_5_102]
				pathway_description_document_value_6_104 = pathway_description_document_value_5_103["document"]
				pathway_description_document_value_7_105 = pathway_description_document_value_6_104["description"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/description", pathway_description_document_value_7_105, None)
				
				# Retrieve value of data property: pathway_title_document
				pathway_title_document_value_0_106 = resource_data_2["MineralSystem"]
				pathway_title_document_index_1_107 = pathway_id_document_index_1_33
				pathway_title_document_value_1_108 = pathway_title_document_value_0_106[pathway_title_document_index_1_107]
				pathway_title_document_value_2_109 = pathway_title_document_value_1_108["pathway"]
				pathway_title_document_index_3_110 = pathway_id_document_index_3_38
				pathway_title_document_value_3_111 = pathway_title_document_value_2_109[pathway_title_document_index_3_110]
				pathway_title_document_value_4_112 = pathway_title_document_value_3_111["supporting_references"]
				pathway_title_document_index_5_113 = pathway_id_document_index_5_43
				pathway_title_document_value_5_114 = pathway_title_document_value_4_112[pathway_title_document_index_5_113]
				pathway_title_document_value_6_115 = pathway_title_document_value_5_114["document"]
				pathway_title_document_value_7_116 = pathway_title_document_value_6_115["title"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/title", pathway_title_document_value_7_116, None)
				
				# Retrieve value of data property: pathway_volume
				pathway_volume_value_0_117 = resource_data_2["MineralSystem"]
				pathway_volume_index_1_118 = pathway_id_document_index_1_33
				pathway_volume_value_1_119 = pathway_volume_value_0_117[pathway_volume_index_1_118]
				pathway_volume_value_2_120 = pathway_volume_value_1_119["pathway"]
				pathway_volume_index_3_121 = pathway_id_document_index_3_38
				pathway_volume_value_3_122 = pathway_volume_value_2_120[pathway_volume_index_3_121]
				pathway_volume_value_4_123 = pathway_volume_value_3_122["supporting_references"]
				pathway_volume_index_5_124 = pathway_id_document_index_5_43
				pathway_volume_value_5_125 = pathway_volume_value_4_123[pathway_volume_index_5_124]
				pathway_volume_value_6_126 = pathway_volume_value_5_125["document"]
				if not ("volume" in pathway_volume_value_6_126):
					pass
				else:
					pathway_volume_value_7_127 = pathway_volume_value_6_126["volume"]
					if True:
						writer_3.write_data_property("https://minmod.isi.edu/resource/volume", pathway_volume_value_7_127, None)
				
				# Retrieve value of data property: pathway_issue_document
				pathway_issue_document_value_0_128 = resource_data_2["MineralSystem"]
				pathway_issue_document_index_1_129 = pathway_id_document_index_1_33
				pathway_issue_document_value_1_130 = pathway_issue_document_value_0_128[pathway_issue_document_index_1_129]
				pathway_issue_document_value_2_131 = pathway_issue_document_value_1_130["pathway"]
				pathway_issue_document_index_3_132 = pathway_id_document_index_3_38
				pathway_issue_document_value_3_133 = pathway_issue_document_value_2_131[pathway_issue_document_index_3_132]
				pathway_issue_document_value_4_134 = pathway_issue_document_value_3_133["supporting_references"]
				pathway_issue_document_index_5_135 = pathway_id_document_index_5_43
				pathway_issue_document_value_5_136 = pathway_issue_document_value_4_134[pathway_issue_document_index_5_135]
				pathway_issue_document_value_6_137 = pathway_issue_document_value_5_136["document"]
				if not ("issue" in pathway_issue_document_value_6_137):
					pass
				else:
					pathway_issue_document_value_7_138 = pathway_issue_document_value_6_137["issue"]
					if True:
						writer_3.write_data_property("https://minmod.isi.edu/resource/issue", pathway_issue_document_value_7_138, None)
				
				# Retrieve value of data property: pathway_month_document
				pathway_month_document_value_0_139 = resource_data_2["MineralSystem"]
				pathway_month_document_index_1_140 = pathway_id_document_index_1_33
				pathway_month_document_value_1_141 = pathway_month_document_value_0_139[pathway_month_document_index_1_140]
				pathway_month_document_value_2_142 = pathway_month_document_value_1_141["pathway"]
				pathway_month_document_index_3_143 = pathway_id_document_index_3_38
				pathway_month_document_value_3_144 = pathway_month_document_value_2_142[pathway_month_document_index_3_143]
				pathway_month_document_value_4_145 = pathway_month_document_value_3_144["supporting_references"]
				pathway_month_document_index_5_146 = pathway_id_document_index_5_43
				pathway_month_document_value_5_147 = pathway_month_document_value_4_145[pathway_month_document_index_5_146]
				pathway_month_document_value_6_148 = pathway_month_document_value_5_147["document"]
				pathway_month_document_value_7_149 = pathway_month_document_value_6_148["month"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/month", pathway_month_document_value_7_149, None)
				
				# Retrieve value of data property: pathway_year_document
				pathway_year_document_value_0_150 = resource_data_2["MineralSystem"]
				pathway_year_document_index_1_151 = pathway_id_document_index_1_33
				pathway_year_document_value_1_152 = pathway_year_document_value_0_150[pathway_year_document_index_1_151]
				pathway_year_document_value_2_153 = pathway_year_document_value_1_152["pathway"]
				pathway_year_document_index_3_154 = pathway_id_document_index_3_38
				pathway_year_document_value_3_155 = pathway_year_document_value_2_153[pathway_year_document_index_3_154]
				pathway_year_document_value_4_156 = pathway_year_document_value_3_155["supporting_references"]
				pathway_year_document_index_5_157 = pathway_id_document_index_5_43
				pathway_year_document_value_5_158 = pathway_year_document_value_4_156[pathway_year_document_index_5_157]
				pathway_year_document_value_6_159 = pathway_year_document_value_5_158["document"]
				pathway_year_document_value_7_160 = pathway_year_document_value_6_159["year"]
				writer_3.write_data_property("https://minmod.isi.edu/resource/year", pathway_year_document_value_7_160, None)
				
				writer_3.end_record()
	
	# Transform records of class mndr:Reference:2
	pathway_id_reference_value_0_161 = resource_data_2["MineralSystem"]
	start_162 = 0
	end_163 = len(pathway_id_reference_value_0_161)
	for pathway_id_reference_index_1_164 in range(start_162, end_163):
		pathway_id_reference_value_1_165 = pathway_id_reference_value_0_161[pathway_id_reference_index_1_164]
		pathway_id_reference_value_2_166 = pathway_id_reference_value_1_165["pathway"]
		start_167 = 0
		end_168 = len(pathway_id_reference_value_2_166)
		for pathway_id_reference_index_3_169 in range(start_167, end_168):
			pathway_id_reference_value_3_170 = pathway_id_reference_value_2_166[pathway_id_reference_index_3_169]
			pathway_id_reference_value_4_171 = pathway_id_reference_value_3_170["supporting_references"]
			start_172 = 0
			end_173 = len(pathway_id_reference_value_4_171)
			for pathway_id_reference_index_5_174 in range(start_172, end_173):
				pathway_id_reference_value_5_175 = pathway_id_reference_value_4_171[pathway_id_reference_index_5_174]
				pathway_id_reference_value_6_176 = pathway_id_reference_value_5_175["id"]
				writer_3.begin_record("https://minmod.isi.edu/resource/Reference", (6, pathway_id_reference_index_1_164, pathway_id_reference_index_3_169, pathway_id_reference_index_5_174), True, False)
				
				# Retrieve value of data property: pathway_id_reference
				writer_3.write_data_property("https://minmod.isi.edu/resource/date", pathway_id_reference_value_6_176, None)
				
				# Retrieve value of object property: pathway_id_document
				pathway_id_document_value_0_177 = resource_data_2["MineralSystem"]
				pathway_id_document_index_1_178 = pathway_id_reference_index_1_164
				pathway_id_document_value_1_179 = pathway_id_document_value_0_177[pathway_id_document_index_1_178]
				pathway_id_document_value_2_180 = pathway_id_document_value_1_179["pathway"]
				pathway_id_document_index_3_181 = pathway_id_reference_index_3_169
				pathway_id_document_value_3_182 = pathway_id_document_value_2_180[pathway_id_document_index_3_181]
				pathway_id_document_value_4_183 = pathway_id_document_value_3_182["supporting_references"]
				pathway_id_document_index_5_184 = pathway_id_reference_index_5_174
				pathway_id_document_value_5_185 = pathway_id_document_value_4_183[pathway_id_document_index_5_184]
				pathway_id_document_value_6_186 = pathway_id_document_value_5_185["document"]
				pathway_id_document_value_7_187 = pathway_id_document_value_6_186["id"]
				writer_3.write_object_property("https://minmod.isi.edu/resource/document", pathway_id_document_value_7_187, True, False, False)
				
				writer_3.end_record()
	
	# Transform records of class mndr:MappableCriteria:2
	pathway_criteria_value_0_188 = resource_data_2["MineralSystem"]
	start_189 = 0
	end_190 = len(pathway_criteria_value_0_188)
	for pathway_criteria_index_1_191 in range(start_189, end_190):
		pathway_criteria_value_1_192 = pathway_criteria_value_0_188[pathway_criteria_index_1_191]
		pathway_criteria_value_2_193 = pathway_criteria_value_1_192["pathway"]
		start_194 = 0
		end_195 = len(pathway_criteria_value_2_193)
		for pathway_criteria_index_3_196 in range(start_194, end_195):
			pathway_criteria_value_3_197 = pathway_criteria_value_2_193[pathway_criteria_index_3_196]
			pathway_criteria_value_4_198 = pathway_criteria_value_3_197["criteria"]
			writer_3.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (2, pathway_criteria_index_1_191, pathway_criteria_index_3_196), True, False)
			
			# Retrieve value of data property: pathway_criteria
			writer_3.write_data_property("https://minmod.isi.edu/resource/criteria", pathway_criteria_value_4_198, None)
			
			# Retrieve value of data property: pathway_theorectical
			pathway_theorectical_value_0_199 = resource_data_2["MineralSystem"]
			pathway_theorectical_index_1_200 = pathway_criteria_index_1_191
			pathway_theorectical_value_1_201 = pathway_theorectical_value_0_199[pathway_theorectical_index_1_200]
			pathway_theorectical_value_2_202 = pathway_theorectical_value_1_201["pathway"]
			pathway_theorectical_index_3_203 = pathway_criteria_index_3_196
			pathway_theorectical_value_3_204 = pathway_theorectical_value_2_202[pathway_theorectical_index_3_203]
			pathway_theorectical_value_4_205 = pathway_theorectical_value_3_204["theorectical"]
			writer_3.write_data_property("https://minmod.isi.edu/resource/theorectical", pathway_theorectical_value_4_205, None)
			
			# Retrieve value of object property: pathway_potential_dataset_name
			pathway_potential_dataset_name_value_0_206 = resource_data_2["MineralSystem"]
			pathway_potential_dataset_name_index_1_207 = pathway_criteria_index_1_191
			pathway_potential_dataset_name_value_1_208 = pathway_potential_dataset_name_value_0_206[pathway_potential_dataset_name_index_1_207]
			pathway_potential_dataset_name_value_2_209 = pathway_potential_dataset_name_value_1_208["pathway"]
			pathway_potential_dataset_name_index_3_210 = pathway_criteria_index_3_196
			pathway_potential_dataset_name_value_3_211 = pathway_potential_dataset_name_value_2_209[pathway_potential_dataset_name_index_3_210]
			pathway_potential_dataset_name_value_4_212 = pathway_potential_dataset_name_value_3_211["potential_dataset"]
			start_213 = 0
			end_214 = len(pathway_potential_dataset_name_value_4_212)
			for pathway_potential_dataset_name_index_5_215 in range(start_213, end_214):
				pathway_potential_dataset_name_value_5_216 = pathway_potential_dataset_name_value_4_212[pathway_potential_dataset_name_index_5_215]
				pathway_potential_dataset_name_value_6_217 = pathway_potential_dataset_name_value_5_216["name"]
				writer_3.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (4, pathway_potential_dataset_name_index_1_207, pathway_potential_dataset_name_index_3_210, pathway_potential_dataset_name_index_5_215), True, True, False)
			
			# Retrieve value of object property: pathway_id_reference
			pathway_id_reference_value_0_218 = resource_data_2["MineralSystem"]
			pathway_id_reference_index_1_219 = pathway_criteria_index_1_191
			pathway_id_reference_value_1_220 = pathway_id_reference_value_0_218[pathway_id_reference_index_1_219]
			pathway_id_reference_value_2_221 = pathway_id_reference_value_1_220["pathway"]
			pathway_id_reference_index_3_222 = pathway_criteria_index_3_196
			pathway_id_reference_value_3_223 = pathway_id_reference_value_2_221[pathway_id_reference_index_3_222]
			pathway_id_reference_value_4_224 = pathway_id_reference_value_3_223["supporting_references"]
			start_225 = 0
			end_226 = len(pathway_id_reference_value_4_224)
			for pathway_id_reference_index_5_227 in range(start_225, end_226):
				pathway_id_reference_value_5_228 = pathway_id_reference_value_4_224[pathway_id_reference_index_5_227]
				pathway_id_reference_value_6_229 = pathway_id_reference_value_5_228["id"]
				writer_3.write_object_property("https://minmod.isi.edu/resource/supporting_references", (6, pathway_id_reference_index_1_219, pathway_id_reference_index_3_222, pathway_id_reference_index_5_227), True, True, False)
			
			writer_3.end_record()
	
	# Transform records of class mndr:MineralSystem:1
	ms_id_value_0_230 = resource_data_2["MineralSystem"]
	start_231 = 0
	end_232 = len(ms_id_value_0_230)
	for ms_id_index_1_233 in range(start_231, end_232):
		ms_id_value_1_234 = ms_id_value_0_230[ms_id_index_1_233]
		ms_id_value_2_235 = ms_id_value_1_234["id"]
		writer_3.begin_record("https://minmod.isi.edu/resource/MineralSystem", (0, ms_id_index_1_233), True, False)
		
		# Retrieve value of data property: ms_id
		writer_3.write_data_property("https://minmod.isi.edu/resource/id", ms_id_value_2_235, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_value_0_236 = resource_data_2["MineralSystem"]
		deposit_type_index_1_237 = ms_id_index_1_233
		deposit_type_value_1_238 = deposit_type_value_0_236[deposit_type_index_1_237]
		deposit_type_value_2_239 = deposit_type_value_1_238["deposit_type"]
		start_240 = 0
		end_241 = len(deposit_type_value_2_239)
		for deposit_type_index_3_242 in range(start_240, end_241):
			deposit_type_value_3_243 = deposit_type_value_2_239[deposit_type_index_3_242]
			writer_3.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_3_243, "https://purl.org/drepr/1.0/uri")
		
		# Retrieve value of object property: pathway_criteria
		pathway_criteria_value_0_244 = resource_data_2["MineralSystem"]
		pathway_criteria_index_1_245 = ms_id_index_1_233
		pathway_criteria_value_1_246 = pathway_criteria_value_0_244[pathway_criteria_index_1_245]
		pathway_criteria_value_2_247 = pathway_criteria_value_1_246["pathway"]
		start_248 = 0
		end_249 = len(pathway_criteria_value_2_247)
		for pathway_criteria_index_3_250 in range(start_248, end_249):
			pathway_criteria_value_3_251 = pathway_criteria_value_2_247[pathway_criteria_index_3_250]
			pathway_criteria_value_4_252 = pathway_criteria_value_3_251["criteria"]
			writer_3.write_object_property("https://minmod.isi.edu/resource/pathway", (2, pathway_criteria_index_1_245, pathway_criteria_index_3_250), True, True, False)
		
		writer_3.end_record()
	
	writer_3.write_to_file(output_file_1)

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])