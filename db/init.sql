CREATE DATABASE db_hosts;
USE db_hosts;
CREATE TABLE iot_device (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac VARCHAR(255) ,
    temp FLOAT,
    time TIMESTAMP
);

INSERT INTO iot_device (mac, temp, time) VALUES
    ('00:11:22:33:44:55', 25.5, '2022-01-22 12:30:00'),
    ('AA:BB:CC:DD:EE:FF', 22.0, '2022-01-22 13:15:00'),
    ('11:22:33:44:55:66', 23.8, '2022-01-22 14:45:00');