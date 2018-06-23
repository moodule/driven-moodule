create table bulk_material (
    id integer primary key,
    name text not null,
    min_density real,
    average_density real,
    max_density real,
    max_belt_speed real,
    max_slope_angle real,
    surcharge_angle real,
    repose_angle real,
    min_lump_size real,
    average_lump_size real,
    max_lump_size real,
    min_lump_ratio real,
    average_lump_ratio real,
    max_lump_ratio real
);