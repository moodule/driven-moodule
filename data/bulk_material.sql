select
bulk_material.id as bulk_material_id,
bulk_material.name as bulk_material_name,
bulk_material.min_density as bulk_material_min_density,
bulk_material.average_density as bulk_material_average_density,
bulk_material.max_density as bulk_material_max_density,
bulk_material.max_belt_speed as bulk_material_max_belt_speed,
bulk_material.max_slope_angle as bulk_material_max_slope_angle,
bulk_material.surcharge_angle as bulk_material_surcharge_angle,
bulk_material.repose_angle as bulk_material_repose_angle,
bulk_material.min_lump_size as bulk_material_min_lump_size,
bulk_material.average_lump_size as bulk_material_average_lump_size,
bulk_material.max_lump_size as bulk_material_max_lump_size,
bulk_material.min_lump_ratio as bulk_material_min_lump_ratio,
bulk_material.average_lump_ratio as bulk_material_average_lump_ratio,
bulk_material.max_lump_ratio as bulk_material_max_lump_ratio,
r_flowability_index.id as flowability_id,
r_flowability_index.id_c3 as flowability_id_c3,
r_flowability_index.name as flowability_name,
r_flowability_index.factor as flowability_factor,
r_abrasion_index.id as abrasion_id,
r_abrasion_index.id_c3 as abrasion_id_c3,
r_abrasion_index.name as abrasion_name,
r_abrasion_index.factor as abrasion_factor,
view_catalog.*
    from bulk_material
    left join r_flowability_index on r_flowability_index.id = bulk_material.flowability_id
    left join r_abrasion_index on r_abrasion_index.id = bulk_material.abrasion_id
    left join l_bulk_material_range on l_bulk_material_range.bulk_material_id = bulk_material.id
    left join view_catalog on view_catalog.range_id = l_bulk_material_range.range_id
order by bulk_material.name;