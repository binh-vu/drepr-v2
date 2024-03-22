from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0, output_file_1):
	resource_data_2 = read_source_json(resource_0)
	
	writer_3 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:DepositTypeCandidate:1
	deposit_type_uri_value_0_4 = resource_data_2["MineralSite"]
	start_5 = 0
	end_6 = len(deposit_type_uri_value_0_4)
	for deposit_type_uri_index_1_7 in range(start_5, end_6):
		deposit_type_uri_value_1_8 = deposit_type_uri_value_0_4[deposit_type_uri_index_1_7]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_8:
			pass
		else:
			deposit_type_uri_value_2_9 = deposit_type_uri_value_1_8["deposit_type_candidate"]
			start_10 = 0
			end_11 = len(deposit_type_uri_value_2_9)
			for deposit_type_uri_index_3_12 in range(start_10, end_11):
				deposit_type_uri_value_3_13 = deposit_type_uri_value_2_9[deposit_type_uri_index_3_12]
				deposit_type_uri_value_4_14 = deposit_type_uri_value_3_13["normalized_uri"]
				writer_3.begin_record("https://minmod.isi.edu/resource/DepositTypeCandidate", (2, deposit_type_uri_index_1_7, deposit_type_uri_index_3_12), True, False)
				
				# Retrieve value of data property: deposit_type_uri
				if True:
					writer_3.write_data_property("https://minmod.isi.edu/resource/normalized_uri", deposit_type_uri_value_4_14, "https://purl.org/drepr/1.0/uri")
				
				writer_3.end_record()
	
	# Transform records of class mndr:MineralSite:1
	site_name_value_0_15 = resource_data_2["MineralSite"]
	start_16 = 0
	end_17 = len(site_name_value_0_15)
	for site_name_index_1_18 in range(start_16, end_17):
		site_name_value_1_19 = site_name_value_0_15[site_name_index_1_18]
		site_name_value_2_20 = site_name_value_1_19["name"]
		writer_3.begin_record("https://minmod.isi.edu/resource/MineralSite", (1, site_name_index_1_18), True, False)
		
		# Retrieve value of data property: site_name
		writer_3.write_data_property("https://minmod.isi.edu/resource/name", site_name_value_2_20, None)
		
		# Retrieve value of data property: site_id
		site_id_value_0_21 = resource_data_2["MineralSite"]
		site_id_index_1_22 = site_name_index_1_18
		site_id_value_1_23 = site_id_value_0_21[site_id_index_1_22]
		site_id_value_2_24 = site_id_value_1_23["record_id"]
		writer_3.write_data_property("https://minmod.isi.edu/resource/record_id", site_id_value_2_24, None)
		
		# Retrieve value of object property: deposit_type_uri
		deposit_type_uri_value_0_25 = resource_data_2["MineralSite"]
		deposit_type_uri_index_1_26 = site_name_index_1_18
		deposit_type_uri_value_1_27 = deposit_type_uri_value_0_25[deposit_type_uri_index_1_26]
		if not ("deposit_type_candidate") in deposit_type_uri_value_1_27:
			pass
		else:
			deposit_type_uri_value_2_28 = deposit_type_uri_value_1_27["deposit_type_candidate"]
			start_29 = 0
			end_30 = len(deposit_type_uri_value_2_28)
			for deposit_type_uri_index_3_31 in range(start_29, end_30):
				deposit_type_uri_value_3_32 = deposit_type_uri_value_2_28[deposit_type_uri_index_3_31]
				deposit_type_uri_value_4_33 = deposit_type_uri_value_3_32["normalized_uri"]
				if writer_3.has_written_record((2, deposit_type_uri_index_1_26, deposit_type_uri_index_3_31)):
					writer_3.write_object_property("https://minmod.isi.edu/resource/deposit_type_candidate", (2, deposit_type_uri_index_1_26, deposit_type_uri_index_3_31), True, True, False)
		
		writer_3.end_record()
	
	writer_3.write_to_file(output_file_1)

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])