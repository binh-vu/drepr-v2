from drepr.readers.prelude import read_source_csv
from drepr.writers.turtle_writer import TurtleWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	writer_2 = TurtleWriter({"mnr": "https://minmod.isi.edu/resource/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mnr:MineralSite:1
	start_3 = 1
	end_4 = len(resource_data_1)
	for a_2013_index_0_5 in range(start_3, end_4):
		a_2013_value_0_6 = resource_data_1[a_2013_index_0_5]
		a_2013_value_1_7 = a_2013_value_0_6[0]
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSite", ("mnr:MineralSite:1", 0, a_2013_index_0_5), True, False)
		
		# Retrieve value of data property: 2013
		writer_2.write_data_property("https://minmod.isi.edu/resource/name", a_2013_value_1_7, None)
		
		# Retrieve value of data property: country
		country_index_0_8 = a_2013_index_0_5
		country_value_0_9 = resource_data_1[country_index_0_8]
		country_value_1_10 = country_value_0_9[1]
		writer_2.write_data_property("https://minmod.isi.edu/resource/country", country_value_1_10, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_index_0_11 = a_2013_index_0_5
		deposit_type_value_0_12 = resource_data_1[deposit_type_index_0_11]
		deposit_type_value_1_13 = deposit_type_value_0_12[2]
		writer_2.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_1_13, None)
		
		writer_2.end_record()
	
	output_14 = writer_2.write_to_string()
	return output_14

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))