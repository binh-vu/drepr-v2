from drepr.readers.prelude import read_source_csv
from drepr.writers.turtle_writer import TurtleWriter

def main(resource_0, output_file_1):
	resource_data_2 = read_source_csv(resource_0)
	
	writer_3 = TurtleWriter({"mnr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mnr:MineralSite:1
	start_4 = 1
	end_5 = len(resource_data_2)
	for a_2013_index_0_6 in range(start_4, end_5):
		a_2013_value_0_7 = resource_data_2[a_2013_index_0_6]
		a_2013_value_1_8 = a_2013_value_0_7[0]
		writer_3.begin_record("https://minmod.isi.edu/resource/MineralSite", ("mnr:MineralSite:1", 0, a_2013_index_0_6), True, False)
		
		# Retrieve value of data property: 2013
		writer_3.write_data_property("https://minmod.isi.edu/resource/name", a_2013_value_1_8, None)
		
		# Retrieve value of data property: country
		country_index_0_9 = a_2013_index_0_6
		country_value_0_10 = resource_data_2[country_index_0_9]
		country_value_1_11 = country_value_0_10[1]
		writer_3.write_data_property("https://minmod.isi.edu/resource/country", country_value_1_11, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_index_0_12 = a_2013_index_0_6
		deposit_type_value_0_13 = resource_data_2[deposit_type_index_0_12]
		deposit_type_value_1_14 = deposit_type_value_0_13[2]
		writer_3.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_1_14, None)
		
		writer_3.end_record()
	
	writer_3.write_to_file(output_file_1)

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])