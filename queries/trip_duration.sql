WITH ranked AS 
(
SELECT ROW_NUMBER() OVER(PARTITION BY DATE(pickup_datetime) ORDER BY DATE_DIFF(dropoff_datetime, pickup_datetime, SECOND) DESC) as rank, *
FROM `fhv_tripdata.fhv_tripdata_2021-02`
)
SELECT DATE_DIFF(dropoff_datetime, pickup_datetime, SECOND) AS trip_duration_seconds, *
FROM ranked
WHERE rank = 1
ORDER BY DATE(pickup_datetime)