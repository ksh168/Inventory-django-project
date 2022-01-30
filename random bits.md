content is the name of the block

5601->kibana

9200->elasticsearch

localhost:9200/company/doc/_search -> to get all documents

localhost:9200/company/doc/ -> method=POST, to add data

localhost:9200/company/doc/1 -> method=POST, to add data with _id=1

localhost:9200/company/ -> method=GET, to see db info

need to add cors to django as well as elaticsearch.yml file