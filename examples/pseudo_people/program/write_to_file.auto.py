from drepr.readers.prelude import read_source_csv
from drepr.writers.turtle_writer import TurtleWriter

def main(resource_0, output_file_1):
	resource_data_2 = read_source_csv(resource_0)
	
	writer_3 = TurtleWriter({"schema": "http://schema.org/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class schema:PostalAddress:1
	start_4 = 1
	end_5 = len(resource_data_2)
	for street_index_0_6 in range(start_4, end_5):
		street_value_0_7 = resource_data_2[street_index_0_6]
		street_value_1_8 = street_value_0_7[3]
		writer_3.begin_record("http://schema.org/PostalAddress", (3, street_index_0_6), True, False)
		
		# Retrieve value of data property: street
		writer_3.write_data_property("http://schema.org/streetAddress", street_value_1_8, None)
		
		# Retrieve value of data property: city
		city_index_0_9 = street_index_0_6
		city_value_0_10 = resource_data_2[city_index_0_9]
		city_value_1_11 = city_value_0_10[4]
		writer_3.write_data_property("http://schema.org/addressLocality", city_value_1_11, None)
		
		# Retrieve value of data property: state
		state_index_0_12 = street_index_0_6
		state_value_0_13 = resource_data_2[state_index_0_12]
		state_value_1_14 = state_value_0_13[5]
		writer_3.write_data_property("http://schema.org/addressRegion", state_value_1_14, None)
		
		# Retrieve value of data property: zipcode
		zipcode_index_0_15 = street_index_0_6
		zipcode_value_0_16 = resource_data_2[zipcode_index_0_15]
		zipcode_value_1_17 = zipcode_value_0_16[6]
		writer_3.write_data_property("http://schema.org/postalCode", zipcode_value_1_17, None)
		
		writer_3.end_record()
	
	# Transform records of class schema:Person:1
	start_18 = 1
	end_19 = len(resource_data_2)
	for id_index_0_20 in range(start_18, end_19):
		id_value_0_21 = resource_data_2[id_index_0_20]
		id_value_1_22 = id_value_0_21[0]
		writer_3.begin_record("http://schema.org/Person", id_value_1_22, False, False)
		
		# Retrieve value of data property: name
		name_index_0_23 = id_index_0_20
		name_value_0_24 = resource_data_2[name_index_0_23]
		name_value_1_25 = name_value_0_24[1]
		writer_3.write_data_property("http://schema.org/name", name_value_1_25, None)
		
		# Retrieve value of data property: phone
		phone_index_0_26 = id_index_0_20
		phone_value_0_27 = resource_data_2[phone_index_0_26]
		phone_value_1_28 = phone_value_0_27[2]
		writer_3.write_data_property("http://schema.org/telephone", phone_value_1_28, None)
		
		# Retrieve value of object property: street
		street_index_0_29 = id_index_0_20
		street_value_0_30 = resource_data_2[street_index_0_29]
		street_value_1_31 = street_value_0_30[3]
		writer_3.write_object_property("http://schema.org/address", (3, street_index_0_29), False, True, False)
		
		writer_3.end_record()
	
	writer_3.write_to_file(output_file_1)

if __name__ == "__main__":
	import sys
	
	main(*sys.argv[1:])