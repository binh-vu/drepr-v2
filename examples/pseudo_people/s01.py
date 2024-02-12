from drepr.readers.prelude import read_source_csv


def main(resource_0):
    resource_data_1 = read_source_csv(resource_0)

    start__local_ast_root_2_2 = 1
    end__local_ast_root_2_3 = len(resource_data_1)
    for street_index_0_4 in range(start__local_ast_root_2_2, end__local_ast_root_2_3):
        street_value_0_5 = resource_data_1[street_index_0_4]
        street_value_1_6 = street_value_0_5[3]

    start__local_ast_root_2_7 = 1
    end__local_ast_root_2_8 = len(resource_data_1)
    for id_index_0_9 in range(start__local_ast_root_2_7, end__local_ast_root_2_8):
        id_value_0_10 = resource_data_1[id_index_0_9]
        id_value_1_11 = id_value_0_10[0]
