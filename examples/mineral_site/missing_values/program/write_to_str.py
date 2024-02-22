from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter


def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#"})
	
	# Transform records of class mndr:DepositTypeCandidate:1
	deposit_type_uri_value_0_3 = resource_data_1["MineralSite"]
	start__local_ast_root__2_6 = 0
	end__local_ast_root__2_7 = len(deposit_type_uri_value_0_3)
	for deposit_type_uri_index_1_4 in range(start__local_ast_root__2_6, end__local_ast_root__2_7):
		deposit_type_uri_value_1_5 = deposit_type_uri_value_0_3[deposit_type_uri_index_1_4]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_5:
			pass
		else:
			deposit_type_uri_value_2_8 = deposit_type_uri_value_1_5["deposit_type_candidate"]
			start__local_ast_root__2__8__2_11 = 0
			end__local_ast_root__2__8__2_12 = len(deposit_type_uri_value_2_8)
			for deposit_type_uri_index_3_9 in range(start__local_ast_root__2__8__2_11, end__local_ast_root__2__8__2_12):
				deposit_type_uri_value_3_10 = deposit_type_uri_value_2_8[deposit_type_uri_index_3_9]
				deposit_type_uri_value_4_13 = deposit_type_uri_value_3_10["normalized_uri"]
				writer_2.begin_record("https://minmod.isi.edu/resource/DepositTypeCandidate", (deposit_type_uri_index_1_4, deposit_type_uri_index_3_9), True, False)
				
				# Retrieve value of data property: deposit_type_uri
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/normalized_uri", deposit_type_uri_value_4_13, "drepr:uri")
				
				writer_2.end_record()
	
	# Transform records of class mndr:MineralSite:1
	site_name_value_0_14 = resource_data_1["MineralSite"]
	start__local_ast_root__2_17 = 0
	end__local_ast_root__2_18 = len(site_name_value_0_14)
	for site_name_index_1_15 in range(start__local_ast_root__2_17, end__local_ast_root__2_18):
		site_name_value_1_16 = site_name_value_0_14[site_name_index_1_15]
		site_name_value_2_19 = site_name_value_1_16["name"]
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSite", site_name_index_1_15, True, False)
		
		# Retrieve value of data property: site_name
		writer_2.write_data_property("https://minmod.isi.edu/resource/name", site_name_value_2_19, None)
		
		# Retrieve value of data property: site_id
		site_id_value_0_20 = resource_data_1["MineralSite"]
		site_id_index_1_21 = site_name_index_1_15
		site_id_value_1_22 = site_id_value_0_20[site_id_index_1_21]
		site_id_value_2_23 = site_id_value_1_22["record_id"]
		writer_2.write_data_property("https://minmod.isi.edu/resource/record_id", site_id_value_2_23, None)
		
		# Retrieve value of object property: deposit_type_uri
		deposit_type_uri_value_0_24 = resource_data_1["MineralSite"]
		deposit_type_uri_index_1_25 = site_name_index_1_15
		deposit_type_uri_value_1_26 = deposit_type_uri_value_0_24[deposit_type_uri_index_1_25]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_26:
			pass
		else:
			deposit_type_uri_value_2_27 = deposit_type_uri_value_1_26["deposit_type_candidate"]
			start__local_ast_root__2__14__19_30 = 0
			end__local_ast_root__2__14__19_31 = len(deposit_type_uri_value_2_27)
			for deposit_type_uri_index_3_28 in range(start__local_ast_root__2__14__19_30, end__local_ast_root__2__14__19_31):
				deposit_type_uri_value_3_29 = deposit_type_uri_value_2_27[deposit_type_uri_index_3_28]
				deposit_type_uri_value_4_32 = deposit_type_uri_value_3_29["normalized_uri"]
				if writer_2.has_written_record((deposit_type_uri_index_1_4, deposit_type_uri_index_3_9)):
					writer_2.write_object_property("https://minmod.isi.edu/resource/deposit_type_candidate", (deposit_type_uri_index_1_4, deposit_type_uri_index_3_9), True, True, False)
		
		writer_2.end_record()
	
	output_33 = writer_2.write_to_string()
	return output_33

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))