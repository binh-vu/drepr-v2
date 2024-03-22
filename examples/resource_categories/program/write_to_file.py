from drepr.readers.prelude import read_source_csv
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0, output_file_1):
	resource_data_2 = read_source_csv(resource_0)
	
	preprocess_0(resource_data_2)
	writer_10 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:ResourceReserveCategory:1
	start_11 = 1
	end_12 = len(resource_data_2)
	for minmod_id_index_0_13 in range(start_11, end_12):
		minmod_id_value_0_14 = resource_data_2[minmod_id_index_0_13]
		minmod_id_value_1_15 = minmod_id_value_0_14[0]
		writer_10.begin_record("https://minmod.isi.edu/resource/ResourceReserveCategory", minmod_id_value_1_15, False, False)
		
		# Retrieve value of data property: name
		name_index_0_16 = minmod_id_index_0_13
		name_value_0_17 = resource_data_2[name_index_0_16]
		name_value_1_18 = name_value_0_17[1]
		writer_10.write_data_property("http://www.w3.org/2000/01/rdf-schema#label", name_value_1_18, "http://www.w3.org/2001/XMLSchema#string")
		
		writer_10.end_record()
	
	writer_10.write_to_file(output_file_1)

def preprocess_0(resource_data_3):
	start_5 = 1
	end_6 = len(resource_data_3)
	for preproc_0_path_index_0_7 in range(start_5, end_6):
		preproc_0_path_value_0_8 = resource_data_3[preproc_0_path_index_0_7]
		preproc_0_path_value_1_9 = preproc_0_path_value_0_8[0]
		preproc_0_path_value_0_8[0] = preproc_0_customfn(preproc_0_path_value_1_9)

def preproc_0_customfn(value):
	return "https://minmod.isi.edu/resource/" + value


if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])