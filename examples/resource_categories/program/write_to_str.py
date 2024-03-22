from drepr.readers.prelude import read_source_csv
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	preprocess_0(resource_data_1)
	writer_9 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:ResourceReserveCategory:1
	start_10 = 1
	end_11 = len(resource_data_1)
	for minmod_id_index_0_12 in range(start_10, end_11):
		minmod_id_value_0_13 = resource_data_1[minmod_id_index_0_12]
		minmod_id_value_1_14 = minmod_id_value_0_13[0]
		writer_9.begin_record("https://minmod.isi.edu/resource/ResourceReserveCategory", minmod_id_value_1_14, False, False)
		
		# Retrieve value of data property: name
		name_index_0_15 = minmod_id_index_0_12
		name_value_0_16 = resource_data_1[name_index_0_15]
		name_value_1_17 = name_value_0_16[1]
		writer_9.write_data_property("http://www.w3.org/2000/01/rdf-schema#label", name_value_1_17, "http://www.w3.org/2001/XMLSchema#string")
		
		writer_9.end_record()
	
	output_18 = writer_9.write_to_string()
	return output_18

def preprocess_0(resource_data_2):
	start_4 = 1
	end_5 = len(resource_data_2)
	for preproc_0_path_index_0_6 in range(start_4, end_5):
		preproc_0_path_value_0_7 = resource_data_2[preproc_0_path_index_0_6]
		preproc_0_path_value_1_8 = preproc_0_path_value_0_7[0]
		preproc_0_path_value_0_7[0] = preproc_0_customfn(preproc_0_path_value_1_8)

def preproc_0_customfn(value):
	return "https://minmod.isi.edu/resource/" + value


if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))