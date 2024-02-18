from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#"})
	
	# Transform records of class mndr:DepositTypeCandidate:1
	writer_2.begin_class("mndr:DepositTypeCandidate:1")
	deposit_type_normalized_uri_value_0_3 = resource_data_1["MineralSite"]
	start__local_ast_root__3_6 = 0
	end__local_ast_root__3_7 = len(deposit_type_normalized_uri_value_0_3)
	for deposit_type_normalized_uri_index_1_4 in range(start__local_ast_root__3_6, end__local_ast_root__3_7):
		deposit_type_normalized_uri_value_1_5 = deposit_type_normalized_uri_value_0_3[deposit_type_normalized_uri_index_1_4]
		deposit_type_normalized_uri_value_2_8 = deposit_type_normalized_uri_value_1_5["deposit_type_candidate"]
		start__local_ast_root__3__9_11 = 0
		end__local_ast_root__3__9_12 = len(deposit_type_normalized_uri_value_2_8)
		for deposit_type_normalized_uri_index_3_9 in range(start__local_ast_root__3__9_11, end__local_ast_root__3__9_12):
			deposit_type_normalized_uri_value_3_10 = deposit_type_normalized_uri_value_2_8[deposit_type_normalized_uri_index_3_9]
			deposit_type_normalized_uri_value_4_13 = deposit_type_normalized_uri_value_3_10["normalized_uri"]
			writer_2.begin_record(deposit_type_normalized_uri_value_4_13, True, False)
			
			# Retrieve value of data property: deposit_type_normalized_uri
			writer_2.write_data_property("https://minmod.isi.edu/resource/normalized_uri", deposit_type_normalized_uri_value_4_13, "drepr:uri")
			
			writer_2.end_record()
	
	# Transform records of class mndr:MineralSite:1
	writer_2.begin_class("mndr:MineralSite:1")
	name_mineral_site_value_0_14 = resource_data_1["MineralSite"]
	start__local_ast_root__3_17 = 0
	end__local_ast_root__3_18 = len(name_mineral_site_value_0_14)
	for name_mineral_site_index_1_15 in range(start__local_ast_root__3_17, end__local_ast_root__3_18):
		name_mineral_site_value_1_16 = name_mineral_site_value_0_14[name_mineral_site_index_1_15]
		name_mineral_site_value_2_19 = name_mineral_site_value_1_16["name"]
		writer_2.begin_record(name_mineral_site_value_2_19, True, False)
		
		# Retrieve value of data property: name_mineral_site
		writer_2.write_data_property("https://minmod.isi.edu/resource/name", name_mineral_site_value_2_19, None)
		
		# Retrieve value of data property: record_mineral_site
		record_mineral_site_value_0_20 = resource_data_1["MineralSite"]
		record_mineral_site_index_1_21 = name_mineral_site_index_1_15
		record_mineral_site_value_1_22 = record_mineral_site_value_0_20[record_mineral_site_index_1_21]
		record_mineral_site_value_2_23 = record_mineral_site_value_1_22["record_id"]
		writer_2.write_data_property("https://minmod.isi.edu/resource/record_id", record_mineral_site_value_2_23, None)
		
		# Retrieve value of object property: deposit_type_normalized_uri
		deposit_type_normalized_uri_value_0_24 = resource_data_1["MineralSite"]
		deposit_type_normalized_uri_index_1_25 = name_mineral_site_index_1_15
		deposit_type_normalized_uri_value_1_26 = deposit_type_normalized_uri_value_0_24[deposit_type_normalized_uri_index_1_25]
		deposit_type_normalized_uri_value_2_27 = deposit_type_normalized_uri_value_1_26["deposit_type_candidate"]
		start__local_ast_root__3__16_30 = 0
		end__local_ast_root__3__16_31 = len(deposit_type_normalized_uri_value_2_27)
		for deposit_type_normalized_uri_index_3_28 in range(start__local_ast_root__3__16_30, end__local_ast_root__3__16_31):
			deposit_type_normalized_uri_value_3_29 = deposit_type_normalized_uri_value_2_27[deposit_type_normalized_uri_index_3_28]
			deposit_type_normalized_uri_value_4_32 = deposit_type_normalized_uri_value_3_29["normalized_uri"]
			writer_2.write_object_property("https://minmod.isi.edu/resource/deposit_type_candidate", deposit_type_normalized_uri_value_4_32, True, True, False)
		
		writer_2.end_record()
	
	output_33 = writer_2.write_to_string()
	return output_33

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])