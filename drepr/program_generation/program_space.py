class VarSpace:
    resource = lambda resource: (f"resource={resource}",)
    resource_data = lambda resource: (f"resource-data={resource}",)
    attr_index_dim = lambda resource, attr, di: (
        f"resource={resource}",
        f"attr={attr}",
        f"index-dim={di}",
    )
    attr_value_dim = lambda resource, attr, di: (
        f"resource={resource}",
        f"attr={attr}",
        f"value-dim={di}",
    )
