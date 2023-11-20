CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    author TEXT, 
    organization TEXT, 
    title TEXT, 
    year INT, 
    source_type TEXT, 
    pages TEXT,
    doi TEXT, 
    owner_id INT
);