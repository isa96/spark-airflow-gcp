SELECT COUNT(*) as count
FROM `fhv_tripdata.fhv_tripdata_2021-02`
WHERE EXTRACT(DAY from pickup_datetime) = 15