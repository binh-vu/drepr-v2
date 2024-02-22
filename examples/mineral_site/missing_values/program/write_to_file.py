from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter


def main(resource_0, output_file_1):
	resource_data_2 = read_source_json(resource_0)
	
	writer_3 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#"})
	
	# Transform records of class mndr:DepositTypeCandidate:1
	deposit_type_uri_value_0_4 = resource_data_2["MineralSite"]
	start__local_ast_root__2_7 = 0
	end__local_ast_root__2_8 = len(deposit_type_uri_value_0_4)
	for deposit_type_uri_index_1_5 in range(start__local_ast_root__2_7, end__local_ast_root__2_8):
		deposit_type_uri_value_1_6 = deposit_type_uri_value_0_4[deposit_type_uri_index_1_5]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_6:
			pass
		else:
			deposit_type_uri_value_2_9 = deposit_type_uri_value_1_6["deposit_type_candidate"]
			start__local_ast_root__2__8__2_12 = 0
			end__local_ast_root__2__8__2_13 = len(deposit_type_uri_value_2_9)
			for deposit_type_uri_index_3_10 in range(start__local_ast_root__2__8__2_12, end__local_ast_root__2__8__2_13):
				deposit_type_uri_value_3_11 = deposit_type_uri_value_2_9[deposit_type_uri_index_3_10]
				deposit_type_uri_value_4_14 = deposit_type_uri_value_3_11["normalized_uri"]
				writer_3.begin_record("https://minmod.isi.edu/resource/DepositTypeCandidate", (deposit_type_uri_index_1_5, deposit_type_uri_index_3_10), True, False)
				
				# Retrieve value of data property: deposit_type_uri
				if True:
					writer_3.write_data_property("https://minmod.isi.edu/resource/normalized_uri", deposit_type_uri_value_4_14, "drepr:uri")
				
				writer_3.end_record()
	
	# Transform records of class mndr:MineralSite:1
	site_name_value_0_15 = resource_data_2["MineralSite"]
	start__local_ast_root__2_18 = 0
	end__local_ast_root__2_19 = len(site_name_value_0_15)
	for site_name_index_1_16 in range(start__local_ast_root__2_18, end__local_ast_root__2_19):
		site_name_value_1_17 = site_name_value_0_15[site_name_index_1_16]
		site_name_value_2_20 = site_name_value_1_17["name"]
		writer_3.begin_record("https://minmod.isi.edu/resource/MineralSite", site_name_index_1_16, True, False)
		
		# Retrieve value of data property: site_name
		writer_3.write_data_property("https://minmod.isi.edu/resource/name", site_name_value_2_20, None)
		
		# Retrieve value of data property: site_id
		site_id_value_0_21 = resource_data_2["MineralSite"]
		site_id_index_1_22 = site_name_index_1_16
		site_id_value_1_23 = site_id_value_0_21[site_id_index_1_22]
		site_id_value_2_24 = site_id_value_1_23["record_id"]
		writer_3.write_data_property("https://minmod.isi.edu/resource/record_id", site_id_value_2_24, None)
		
		# Retrieve value of object property: deposit_type_uri
		deposit_type_uri_value_0_25 = resource_data_2["MineralSite"]
		deposit_type_uri_index_1_26 = site_name_index_1_16
		deposit_type_uri_value_1_27 = deposit_type_uri_value_0_25[deposit_type_uri_index_1_26]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_27:
			pass
		else:
			deposit_type_uri_value_2_28 = deposit_type_uri_value_1_27["deposit_type_candidate"]
			start__local_ast_root__2__14__19_31 = 0
			end__local_ast_root__2__14__19_32 = len(deposit_type_uri_value_2_28)
			for deposit_type_uri_index_3_29 in range(start__local_ast_root__2__14__19_31, end__local_ast_root__2__14__19_32):
				deposit_type_uri_value_3_30 = deposit_type_uri_value_2_28[deposit_type_uri_index_3_29]
				deposit_type_uri_value_4_33 = deposit_type_uri_value_3_30["normalized_uri"]
				if writer_3.has_written_record((deposit_type_uri_index_1_5, deposit_type_uri_index_3_10)):
					writer_3.write_object_property("https://minmod.isi.edu/resource/deposit_type_candidate", (deposit_type_uri_index_1_5, deposit_type_uri_index_3_10), True, True, False)
		
		writer_3.end_record()
	
	writer_3.write_to_file(output_file_1)

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])