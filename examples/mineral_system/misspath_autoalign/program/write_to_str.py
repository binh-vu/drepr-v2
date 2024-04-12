from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "geokb": "https://geokb.wikibase.cloud/entity/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "xsd": "http://www.w3.org/2001/XMLSchema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "geo": "http://www.opengis.net/ont/geosparql#", "gkbi": "https://geokb.wikibase.cloud/entity/", "gkbp": "https://geokb.wikibase.cloud/wiki/Property/"})
	
	# Transform records of class mndr:EvidenceLayer:2
	pathway_potential_dataset_name_value_0_3 = resource_data_1["MineralSystem"]
	start_4 = 0
	end_5 = len(pathway_potential_dataset_name_value_0_3)
	for pathway_potential_dataset_name_index_1_6 in range(start_4, end_5):
		pathway_potential_dataset_name_value_1_7 = pathway_potential_dataset_name_value_0_3[pathway_potential_dataset_name_index_1_6]
		pathway_potential_dataset_name_value_2_8 = pathway_potential_dataset_name_value_1_7["pathway"]
		start_9 = 0
		end_10 = len(pathway_potential_dataset_name_value_2_8)
		for pathway_potential_dataset_name_index_3_11 in range(start_9, end_10):
			pathway_potential_dataset_name_value_3_12 = pathway_potential_dataset_name_value_2_8[pathway_potential_dataset_name_index_3_11]
			pathway_potential_dataset_name_value_4_13 = pathway_potential_dataset_name_value_3_12["potential_dataset"]
			start_14 = 0
			end_15 = len(pathway_potential_dataset_name_value_4_13)
			for pathway_potential_dataset_name_index_5_16 in range(start_14, end_15):
				pathway_potential_dataset_name_value_5_17 = pathway_potential_dataset_name_value_4_13[pathway_potential_dataset_name_index_5_16]
				pathway_potential_dataset_name_value_6_18 = pathway_potential_dataset_name_value_5_17["name"]
				writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (4, pathway_potential_dataset_name_index_1_6, pathway_potential_dataset_name_index_3_11, pathway_potential_dataset_name_index_5_16), True, False)
				
				# Retrieve value of data property: pathway_potential_dataset_name
				writer_2.write_data_property("https://minmod.isi.edu/resource/name", pathway_potential_dataset_name_value_6_18, None)
				
				# Retrieve value of data property: pathway_potential_dataset_score
				pathway_potential_dataset_score_value_0_19 = resource_data_1["MineralSystem"]
				pathway_potential_dataset_score_index_1_20 = pathway_potential_dataset_name_index_1_6
				pathway_potential_dataset_score_value_1_21 = pathway_potential_dataset_score_value_0_19[pathway_potential_dataset_score_index_1_20]
				pathway_potential_dataset_score_value_2_22 = pathway_potential_dataset_score_value_1_21["pathway"]
				pathway_potential_dataset_score_index_3_23 = pathway_potential_dataset_name_index_3_11
				pathway_potential_dataset_score_value_3_24 = pathway_potential_dataset_score_value_2_22[pathway_potential_dataset_score_index_3_23]
				pathway_potential_dataset_score_value_4_25 = pathway_potential_dataset_score_value_3_24["potential_dataset"]
				pathway_potential_dataset_score_index_5_26 = pathway_potential_dataset_name_index_5_16
				pathway_potential_dataset_score_value_5_27 = pathway_potential_dataset_score_value_4_25[pathway_potential_dataset_score_index_5_26]
				pathway_potential_dataset_score_value_6_28 = pathway_potential_dataset_score_value_5_27["relevance_score"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", pathway_potential_dataset_score_value_6_28, None)
				
				writer_2.end_record()
	
	# Transform records of class mndr:Document:2
	pathway_id_document_value_0_29 = resource_data_1["MineralSystem"]
	start_30 = 0
	end_31 = len(pathway_id_document_value_0_29)
	for pathway_id_document_index_1_32 in range(start_30, end_31):
		pathway_id_document_value_1_33 = pathway_id_document_value_0_29[pathway_id_document_index_1_32]
		pathway_id_document_value_2_34 = pathway_id_document_value_1_33["pathway"]
		start_35 = 0
		end_36 = len(pathway_id_document_value_2_34)
		for pathway_id_document_index_3_37 in range(start_35, end_36):
			pathway_id_document_value_3_38 = pathway_id_document_value_2_34[pathway_id_document_index_3_37]
			pathway_id_document_value_4_39 = pathway_id_document_value_3_38["supporting_references"]
			start_40 = 0
			end_41 = len(pathway_id_document_value_4_39)
			for pathway_id_document_index_5_42 in range(start_40, end_41):
				pathway_id_document_value_5_43 = pathway_id_document_value_4_39[pathway_id_document_index_5_42]
				pathway_id_document_value_6_44 = pathway_id_document_value_5_43["document"]
				pathway_id_document_value_7_45 = pathway_id_document_value_6_44["id"]
				writer_2.begin_record("https://minmod.isi.edu/resource/Document", pathway_id_document_value_7_45, False, False)
				
				# Retrieve value of data property: pathway_id_document
				writer_2.write_data_property("https://minmod.isi.edu/resource/id", pathway_id_document_value_7_45, None)
				
				# Retrieve value of data property: pathway_uri_document
				pathway_uri_document_value_0_46 = resource_data_1["MineralSystem"]
				pathway_uri_document_index_1_47 = pathway_id_document_index_1_32
				pathway_uri_document_value_1_48 = pathway_uri_document_value_0_46[pathway_uri_document_index_1_47]
				pathway_uri_document_value_2_49 = pathway_uri_document_value_1_48["pathway"]
				pathway_uri_document_index_3_50 = pathway_id_document_index_3_37
				pathway_uri_document_value_3_51 = pathway_uri_document_value_2_49[pathway_uri_document_index_3_50]
				pathway_uri_document_value_4_52 = pathway_uri_document_value_3_51["supporting_references"]
				pathway_uri_document_index_5_53 = pathway_id_document_index_5_42
				pathway_uri_document_value_5_54 = pathway_uri_document_value_4_52[pathway_uri_document_index_5_53]
				pathway_uri_document_value_6_55 = pathway_uri_document_value_5_54["document"]
				pathway_uri_document_value_7_56 = pathway_uri_document_value_6_55["uri"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/uri", pathway_uri_document_value_7_56, None)
				
				# Retrieve value of data property: pathway_doi
				pathway_doi_value_0_57 = resource_data_1["MineralSystem"]
				pathway_doi_index_1_58 = pathway_id_document_index_1_32
				pathway_doi_value_1_59 = pathway_doi_value_0_57[pathway_doi_index_1_58]
				pathway_doi_value_2_60 = pathway_doi_value_1_59["pathway"]
				pathway_doi_index_3_61 = pathway_id_document_index_3_37
				pathway_doi_value_3_62 = pathway_doi_value_2_60[pathway_doi_index_3_61]
				pathway_doi_value_4_63 = pathway_doi_value_3_62["supporting_references"]
				pathway_doi_index_5_64 = pathway_id_document_index_5_42
				pathway_doi_value_5_65 = pathway_doi_value_4_63[pathway_doi_index_5_64]
				pathway_doi_value_6_66 = pathway_doi_value_5_65["document"]
				pathway_doi_value_7_67 = pathway_doi_value_6_66["doi"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/doi", pathway_doi_value_7_67, None)
				
				# Retrieve value of data property: pathway_journal
				pathway_journal_value_0_68 = resource_data_1["MineralSystem"]
				pathway_journal_index_1_69 = pathway_id_document_index_1_32
				pathway_journal_value_1_70 = pathway_journal_value_0_68[pathway_journal_index_1_69]
				pathway_journal_value_2_71 = pathway_journal_value_1_70["pathway"]
				pathway_journal_index_3_72 = pathway_id_document_index_3_37
				pathway_journal_value_3_73 = pathway_journal_value_2_71[pathway_journal_index_3_72]
				pathway_journal_value_4_74 = pathway_journal_value_3_73["supporting_references"]
				pathway_journal_index_5_75 = pathway_id_document_index_5_42
				pathway_journal_value_5_76 = pathway_journal_value_4_74[pathway_journal_index_5_75]
				pathway_journal_value_6_77 = pathway_journal_value_5_76["document"]
				if not ("journal" in pathway_journal_value_6_77):
					pass
				else:
					pathway_journal_value_7_78 = pathway_journal_value_6_77["journal"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/journal", pathway_journal_value_7_78, None)
				
				# Retrieve value of data property: pathway_authors
				pathway_authors_value_0_79 = resource_data_1["MineralSystem"]
				pathway_authors_index_1_80 = pathway_id_document_index_1_32
				pathway_authors_value_1_81 = pathway_authors_value_0_79[pathway_authors_index_1_80]
				pathway_authors_value_2_82 = pathway_authors_value_1_81["pathway"]
				pathway_authors_index_3_83 = pathway_id_document_index_3_37
				pathway_authors_value_3_84 = pathway_authors_value_2_82[pathway_authors_index_3_83]
				pathway_authors_value_4_85 = pathway_authors_value_3_84["supporting_references"]
				pathway_authors_index_5_86 = pathway_id_document_index_5_42
				pathway_authors_value_5_87 = pathway_authors_value_4_85[pathway_authors_index_5_86]
				pathway_authors_value_6_88 = pathway_authors_value_5_87["document"]
				pathway_authors_value_7_89 = pathway_authors_value_6_88["authors"]
				start_90 = 0
				end_91 = len(pathway_authors_value_7_89)
				for pathway_authors_index_8_92 in range(start_90, end_91):
					pathway_authors_value_8_93 = pathway_authors_value_7_89[pathway_authors_index_8_92]
					writer_2.write_data_property("https://minmod.isi.edu/resource/authors", pathway_authors_value_8_93, None)
				
				# Retrieve value of data property: pathway_description_document
				pathway_description_document_value_0_94 = resource_data_1["MineralSystem"]
				pathway_description_document_index_1_95 = pathway_id_document_index_1_32
				pathway_description_document_value_1_96 = pathway_description_document_value_0_94[pathway_description_document_index_1_95]
				pathway_description_document_value_2_97 = pathway_description_document_value_1_96["pathway"]
				pathway_description_document_index_3_98 = pathway_id_document_index_3_37
				pathway_description_document_value_3_99 = pathway_description_document_value_2_97[pathway_description_document_index_3_98]
				pathway_description_document_value_4_100 = pathway_description_document_value_3_99["supporting_references"]
				pathway_description_document_index_5_101 = pathway_id_document_index_5_42
				pathway_description_document_value_5_102 = pathway_description_document_value_4_100[pathway_description_document_index_5_101]
				pathway_description_document_value_6_103 = pathway_description_document_value_5_102["document"]
				pathway_description_document_value_7_104 = pathway_description_document_value_6_103["description"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/description", pathway_description_document_value_7_104, None)
				
				# Retrieve value of data property: pathway_title_document
				pathway_title_document_value_0_105 = resource_data_1["MineralSystem"]
				pathway_title_document_index_1_106 = pathway_id_document_index_1_32
				pathway_title_document_value_1_107 = pathway_title_document_value_0_105[pathway_title_document_index_1_106]
				pathway_title_document_value_2_108 = pathway_title_document_value_1_107["pathway"]
				pathway_title_document_index_3_109 = pathway_id_document_index_3_37
				pathway_title_document_value_3_110 = pathway_title_document_value_2_108[pathway_title_document_index_3_109]
				pathway_title_document_value_4_111 = pathway_title_document_value_3_110["supporting_references"]
				pathway_title_document_index_5_112 = pathway_id_document_index_5_42
				pathway_title_document_value_5_113 = pathway_title_document_value_4_111[pathway_title_document_index_5_112]
				pathway_title_document_value_6_114 = pathway_title_document_value_5_113["document"]
				pathway_title_document_value_7_115 = pathway_title_document_value_6_114["title"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/title", pathway_title_document_value_7_115, None)
				
				# Retrieve value of data property: pathway_volume
				pathway_volume_value_0_116 = resource_data_1["MineralSystem"]
				pathway_volume_index_1_117 = pathway_id_document_index_1_32
				pathway_volume_value_1_118 = pathway_volume_value_0_116[pathway_volume_index_1_117]
				pathway_volume_value_2_119 = pathway_volume_value_1_118["pathway"]
				pathway_volume_index_3_120 = pathway_id_document_index_3_37
				pathway_volume_value_3_121 = pathway_volume_value_2_119[pathway_volume_index_3_120]
				pathway_volume_value_4_122 = pathway_volume_value_3_121["supporting_references"]
				pathway_volume_index_5_123 = pathway_id_document_index_5_42
				pathway_volume_value_5_124 = pathway_volume_value_4_122[pathway_volume_index_5_123]
				pathway_volume_value_6_125 = pathway_volume_value_5_124["document"]
				if not ("volume" in pathway_volume_value_6_125):
					pass
				else:
					pathway_volume_value_7_126 = pathway_volume_value_6_125["volume"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/volume", pathway_volume_value_7_126, None)
				
				# Retrieve value of data property: pathway_issue_document
				pathway_issue_document_value_0_127 = resource_data_1["MineralSystem"]
				pathway_issue_document_index_1_128 = pathway_id_document_index_1_32
				pathway_issue_document_value_1_129 = pathway_issue_document_value_0_127[pathway_issue_document_index_1_128]
				pathway_issue_document_value_2_130 = pathway_issue_document_value_1_129["pathway"]
				pathway_issue_document_index_3_131 = pathway_id_document_index_3_37
				pathway_issue_document_value_3_132 = pathway_issue_document_value_2_130[pathway_issue_document_index_3_131]
				pathway_issue_document_value_4_133 = pathway_issue_document_value_3_132["supporting_references"]
				pathway_issue_document_index_5_134 = pathway_id_document_index_5_42
				pathway_issue_document_value_5_135 = pathway_issue_document_value_4_133[pathway_issue_document_index_5_134]
				pathway_issue_document_value_6_136 = pathway_issue_document_value_5_135["document"]
				if not ("issue" in pathway_issue_document_value_6_136):
					pass
				else:
					pathway_issue_document_value_7_137 = pathway_issue_document_value_6_136["issue"]
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/issue", pathway_issue_document_value_7_137, None)
				
				# Retrieve value of data property: pathway_month_document
				pathway_month_document_value_0_138 = resource_data_1["MineralSystem"]
				pathway_month_document_index_1_139 = pathway_id_document_index_1_32
				pathway_month_document_value_1_140 = pathway_month_document_value_0_138[pathway_month_document_index_1_139]
				pathway_month_document_value_2_141 = pathway_month_document_value_1_140["pathway"]
				pathway_month_document_index_3_142 = pathway_id_document_index_3_37
				pathway_month_document_value_3_143 = pathway_month_document_value_2_141[pathway_month_document_index_3_142]
				pathway_month_document_value_4_144 = pathway_month_document_value_3_143["supporting_references"]
				pathway_month_document_index_5_145 = pathway_id_document_index_5_42
				pathway_month_document_value_5_146 = pathway_month_document_value_4_144[pathway_month_document_index_5_145]
				pathway_month_document_value_6_147 = pathway_month_document_value_5_146["document"]
				pathway_month_document_value_7_148 = pathway_month_document_value_6_147["month"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/month", pathway_month_document_value_7_148, None)
				
				# Retrieve value of data property: pathway_year_document
				pathway_year_document_value_0_149 = resource_data_1["MineralSystem"]
				pathway_year_document_index_1_150 = pathway_id_document_index_1_32
				pathway_year_document_value_1_151 = pathway_year_document_value_0_149[pathway_year_document_index_1_150]
				pathway_year_document_value_2_152 = pathway_year_document_value_1_151["pathway"]
				pathway_year_document_index_3_153 = pathway_id_document_index_3_37
				pathway_year_document_value_3_154 = pathway_year_document_value_2_152[pathway_year_document_index_3_153]
				pathway_year_document_value_4_155 = pathway_year_document_value_3_154["supporting_references"]
				pathway_year_document_index_5_156 = pathway_id_document_index_5_42
				pathway_year_document_value_5_157 = pathway_year_document_value_4_155[pathway_year_document_index_5_156]
				pathway_year_document_value_6_158 = pathway_year_document_value_5_157["document"]
				pathway_year_document_value_7_159 = pathway_year_document_value_6_158["year"]
				writer_2.write_data_property("https://minmod.isi.edu/resource/year", pathway_year_document_value_7_159, None)
				
				writer_2.end_record()
	
	# Transform records of class mndr:Reference:2
	pathway_id_reference_value_0_160 = resource_data_1["MineralSystem"]
	start_161 = 0
	end_162 = len(pathway_id_reference_value_0_160)
	for pathway_id_reference_index_1_163 in range(start_161, end_162):
		pathway_id_reference_value_1_164 = pathway_id_reference_value_0_160[pathway_id_reference_index_1_163]
		pathway_id_reference_value_2_165 = pathway_id_reference_value_1_164["pathway"]
		start_166 = 0
		end_167 = len(pathway_id_reference_value_2_165)
		for pathway_id_reference_index_3_168 in range(start_166, end_167):
			pathway_id_reference_value_3_169 = pathway_id_reference_value_2_165[pathway_id_reference_index_3_168]
			pathway_id_reference_value_4_170 = pathway_id_reference_value_3_169["supporting_references"]
			start_171 = 0
			end_172 = len(pathway_id_reference_value_4_170)
			for pathway_id_reference_index_5_173 in range(start_171, end_172):
				pathway_id_reference_value_5_174 = pathway_id_reference_value_4_170[pathway_id_reference_index_5_173]
				pathway_id_reference_value_6_175 = pathway_id_reference_value_5_174["id"]
				writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (6, pathway_id_reference_index_1_163, pathway_id_reference_index_3_168, pathway_id_reference_index_5_173), True, False)
				
				# Retrieve value of data property: pathway_id_reference
				writer_2.write_data_property("https://minmod.isi.edu/resource/date", pathway_id_reference_value_6_175, None)
				
				# Retrieve value of object property: pathway_id_document
				pathway_id_document_value_0_176 = resource_data_1["MineralSystem"]
				pathway_id_document_index_1_177 = pathway_id_reference_index_1_163
				pathway_id_document_value_1_178 = pathway_id_document_value_0_176[pathway_id_document_index_1_177]
				pathway_id_document_value_2_179 = pathway_id_document_value_1_178["pathway"]
				pathway_id_document_index_3_180 = pathway_id_reference_index_3_168
				pathway_id_document_value_3_181 = pathway_id_document_value_2_179[pathway_id_document_index_3_180]
				pathway_id_document_value_4_182 = pathway_id_document_value_3_181["supporting_references"]
				pathway_id_document_index_5_183 = pathway_id_reference_index_5_173
				pathway_id_document_value_5_184 = pathway_id_document_value_4_182[pathway_id_document_index_5_183]
				pathway_id_document_value_6_185 = pathway_id_document_value_5_184["document"]
				pathway_id_document_value_7_186 = pathway_id_document_value_6_185["id"]
				writer_2.write_object_property("https://minmod.isi.edu/resource/document", pathway_id_document_value_7_186, True, False, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:2
	pathway_criteria_value_0_187 = resource_data_1["MineralSystem"]
	start_188 = 0
	end_189 = len(pathway_criteria_value_0_187)
	for pathway_criteria_index_1_190 in range(start_188, end_189):
		pathway_criteria_value_1_191 = pathway_criteria_value_0_187[pathway_criteria_index_1_190]
		pathway_criteria_value_2_192 = pathway_criteria_value_1_191["pathway"]
		start_193 = 0
		end_194 = len(pathway_criteria_value_2_192)
		for pathway_criteria_index_3_195 in range(start_193, end_194):
			pathway_criteria_value_3_196 = pathway_criteria_value_2_192[pathway_criteria_index_3_195]
			pathway_criteria_value_4_197 = pathway_criteria_value_3_196["criteria"]
			writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (2, pathway_criteria_index_1_190, pathway_criteria_index_3_195), True, False)
			
			# Retrieve value of data property: pathway_criteria
			writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", pathway_criteria_value_4_197, None)
			
			# Retrieve value of data property: pathway_theorectical
			pathway_theorectical_value_0_198 = resource_data_1["MineralSystem"]
			pathway_theorectical_index_1_199 = pathway_criteria_index_1_190
			pathway_theorectical_value_1_200 = pathway_theorectical_value_0_198[pathway_theorectical_index_1_199]
			pathway_theorectical_value_2_201 = pathway_theorectical_value_1_200["pathway"]
			pathway_theorectical_index_3_202 = pathway_criteria_index_3_195
			pathway_theorectical_value_3_203 = pathway_theorectical_value_2_201[pathway_theorectical_index_3_202]
			pathway_theorectical_value_4_204 = pathway_theorectical_value_3_203["theorectical"]
			writer_2.write_data_property("https://minmod.isi.edu/resource/theorectical", pathway_theorectical_value_4_204, None)
			
			# Retrieve value of object property: pathway_potential_dataset_name
			pathway_potential_dataset_name_value_0_205 = resource_data_1["MineralSystem"]
			pathway_potential_dataset_name_index_1_206 = pathway_criteria_index_1_190
			pathway_potential_dataset_name_value_1_207 = pathway_potential_dataset_name_value_0_205[pathway_potential_dataset_name_index_1_206]
			pathway_potential_dataset_name_value_2_208 = pathway_potential_dataset_name_value_1_207["pathway"]
			pathway_potential_dataset_name_index_3_209 = pathway_criteria_index_3_195
			pathway_potential_dataset_name_value_3_210 = pathway_potential_dataset_name_value_2_208[pathway_potential_dataset_name_index_3_209]
			pathway_potential_dataset_name_value_4_211 = pathway_potential_dataset_name_value_3_210["potential_dataset"]
			start_212 = 0
			end_213 = len(pathway_potential_dataset_name_value_4_211)
			for pathway_potential_dataset_name_index_5_214 in range(start_212, end_213):
				pathway_potential_dataset_name_value_5_215 = pathway_potential_dataset_name_value_4_211[pathway_potential_dataset_name_index_5_214]
				pathway_potential_dataset_name_value_6_216 = pathway_potential_dataset_name_value_5_215["name"]
				writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (4, pathway_potential_dataset_name_index_1_206, pathway_potential_dataset_name_index_3_209, pathway_potential_dataset_name_index_5_214), True, True, False)
			
			# Retrieve value of object property: pathway_id_reference
			pathway_id_reference_value_0_217 = resource_data_1["MineralSystem"]
			pathway_id_reference_index_1_218 = pathway_criteria_index_1_190
			pathway_id_reference_value_1_219 = pathway_id_reference_value_0_217[pathway_id_reference_index_1_218]
			pathway_id_reference_value_2_220 = pathway_id_reference_value_1_219["pathway"]
			pathway_id_reference_index_3_221 = pathway_criteria_index_3_195
			pathway_id_reference_value_3_222 = pathway_id_reference_value_2_220[pathway_id_reference_index_3_221]
			pathway_id_reference_value_4_223 = pathway_id_reference_value_3_222["supporting_references"]
			start_224 = 0
			end_225 = len(pathway_id_reference_value_4_223)
			for pathway_id_reference_index_5_226 in range(start_224, end_225):
				pathway_id_reference_value_5_227 = pathway_id_reference_value_4_223[pathway_id_reference_index_5_226]
				pathway_id_reference_value_6_228 = pathway_id_reference_value_5_227["id"]
				writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (6, pathway_id_reference_index_1_218, pathway_id_reference_index_3_221, pathway_id_reference_index_5_226), True, True, False)
			
			writer_2.end_record()
	
	# Transform records of class mndr:MineralSystem:1
	ms_id_value_0_229 = resource_data_1["MineralSystem"]
	start_230 = 0
	end_231 = len(ms_id_value_0_229)
	for ms_id_index_1_232 in range(start_230, end_231):
		ms_id_value_1_233 = ms_id_value_0_229[ms_id_index_1_232]
		ms_id_value_2_234 = ms_id_value_1_233["id"]
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSystem", (0, ms_id_index_1_232), True, False)
		
		# Retrieve value of data property: ms_id
		writer_2.write_data_property("https://minmod.isi.edu/resource/id", ms_id_value_2_234, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_value_0_235 = resource_data_1["MineralSystem"]
		deposit_type_index_1_236 = ms_id_index_1_232
		deposit_type_value_1_237 = deposit_type_value_0_235[deposit_type_index_1_236]
		deposit_type_value_2_238 = deposit_type_value_1_237["deposit_type"]
		start_239 = 0
		end_240 = len(deposit_type_value_2_238)
		for deposit_type_index_3_241 in range(start_239, end_240):
			deposit_type_value_3_242 = deposit_type_value_2_238[deposit_type_index_3_241]
			writer_2.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_3_242, "https://purl.org/drepr/1.0/uri")
		
		# Retrieve value of object property: pathway_criteria
		pathway_criteria_value_0_243 = resource_data_1["MineralSystem"]
		pathway_criteria_index_1_244 = ms_id_index_1_232
		pathway_criteria_value_1_245 = pathway_criteria_value_0_243[pathway_criteria_index_1_244]
		pathway_criteria_value_2_246 = pathway_criteria_value_1_245["pathway"]
		start_247 = 0
		end_248 = len(pathway_criteria_value_2_246)
		for pathway_criteria_index_3_249 in range(start_247, end_248):
			pathway_criteria_value_3_250 = pathway_criteria_value_2_246[pathway_criteria_index_3_249]
			pathway_criteria_value_4_251 = pathway_criteria_value_3_250["criteria"]
			writer_2.write_object_property("https://minmod.isi.edu/resource/pathway", (2, pathway_criteria_index_1_244, pathway_criteria_index_3_249), True, True, False)
		
		writer_2.end_record()
	
	output_252 = writer_2.write_to_string()
	return output_252

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))