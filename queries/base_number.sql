SELECT dispatching_base_num, COUNT(*) as count
FROM `fhv_tripdata.fhv_tripdata_2021-02`
GROUP BY dispatching_base_num
ORDER BY count DESC
LIMIT 5