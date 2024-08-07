from drepr.readers.prelude import read_source_csv
from drepr.writers.turtle_writer import TurtleWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	writer_2 = TurtleWriter({"schema": "http://schema.org/", "drepr": "https://purl.org/drepr/1.0/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class schema:PostalAddress:1
	start_3 = 1
	end_4 = len(resource_data_1)
	for street_index_0_5 in range(start_3, end_4):
		street_value_0_6 = resource_data_1[street_index_0_5]
		street_value_1_7 = street_value_0_6[3]
		writer_2.begin_record("http://schema.org/PostalAddress", (3, street_index_0_5), True, False)
		
		# Retrieve value of data property: street
		writer_2.write_data_property("http://schema.org/streetAddress", street_value_1_7, None)
		
		# Retrieve value of data property: city
		city_index_0_8 = street_index_0_5
		city_value_0_9 = resource_data_1[city_index_0_8]
		city_value_1_10 = city_value_0_9[4]
		writer_2.write_data_property("http://schema.org/addressLocality", city_value_1_10, None)
		
		# Retrieve value of data property: state
		state_index_0_11 = street_index_0_5
		state_value_0_12 = resource_data_1[state_index_0_11]
		state_value_1_13 = state_value_0_12[5]
		writer_2.write_data_property("http://schema.org/addressRegion", state_value_1_13, None)
		
		# Retrieve value of data property: zipcode
		zipcode_index_0_14 = street_index_0_5
		zipcode_value_0_15 = resource_data_1[zipcode_index_0_14]
		zipcode_value_1_16 = zipcode_value_0_15[6]
		writer_2.write_data_property("http://schema.org/postalCode", zipcode_value_1_16, None)
		
		writer_2.end_record()
	
	# Transform records of class schema:Person:1
	start_17 = 1
	end_18 = len(resource_data_1)
	for id_index_0_19 in range(start_17, end_18):
		id_value_0_20 = resource_data_1[id_index_0_19]
		id_value_1_21 = id_value_0_20[0]
		writer_2.begin_record("http://schema.org/Person", id_value_1_21, False, False)
		
		# Retrieve value of data property: name
		name_index_0_22 = id_index_0_19
		name_value_0_23 = resource_data_1[name_index_0_22]
		name_value_1_24 = name_value_0_23[1]
		writer_2.write_data_property("http://schema.org/name", name_value_1_24, None)
		
		# Retrieve value of data property: phone
		phone_index_0_25 = id_index_0_19
		phone_value_0_26 = resource_data_1[phone_index_0_25]
		phone_value_1_27 = phone_value_0_26[2]
		writer_2.write_data_property("http://schema.org/telephone", phone_value_1_27, None)
		
		# Retrieve value of object property: street
		street_index_0_28 = id_index_0_19
		street_value_0_29 = resource_data_1[street_index_0_28]
		street_value_1_30 = street_value_0_29[3]
		writer_2.write_object_property("http://schema.org/address", (3, street_index_0_28), False, True, False)
		
		writer_2.end_record()
	
	output_31 = writer_2.write_to_string()
	return output_31

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))