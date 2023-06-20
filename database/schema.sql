CREATE TABLE IF NOT EXISTS 'blacklist' (
  'user_id' varchar(20) NOT NULL,
  'created_at' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'warns' (
  'id' int(11) NOT NULL,
  'user_id' varchar(20) NOT NULL,
  'server_id' varchar(20) NOT NULL,
  'moderator_id' varchar(20) NOT NULL,
  'reason' varchar(255) NOT NULL,
  'created_at' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'states' (
    'user_id' varchar(20) NOT NULL,
    'location' varchar(255) NOT NULL DEFAULT 'start',
    'inventory_json' varchar(5000000000) NOT NULL DEFAULT '[]',
    'updated_time' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);