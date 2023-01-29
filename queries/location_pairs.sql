SELECT PUlocationID, DOlocationID, COUNT(*) as count
FROM `fhv_tripdata.fhv_tripdata_2021-02`
WHERE PUlocationID IS NOT NULL AND DOlocationID IS NOT NULL
GROUP BY PUlocationID, DOlocationID
ORDER BY count DESC
LIMIT 5