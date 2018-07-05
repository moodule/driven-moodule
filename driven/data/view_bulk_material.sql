select
    id,
    name,
    min_density,
    average_density,
    max_density,
    max_belt_speed,
    max_slope_angle,
    surcharge_angle,
    repose_angle,
    min_lump_size,
    average_lump_size,
    max_lump_size,
    min_lump_ratio,
    average_lump_ratio,
    max_lump_ratio
from bulk_material
order by name;