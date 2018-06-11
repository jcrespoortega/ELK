# Logstash
Before use this tool you must create an index in ElastichSearch:

$ ./bin/elasticsearch

$ curl -X PUT "localhost:9200/lugares" -H 'Content-Type: application/json' -d'{
	"settings" : {"number_of_shards" : 1},
	"mappings" : {
		"restaurantes": 
			{"properties" : 
				{"location" : { "type": "geo_point"}}
			}
		}
	}'

Logstash is the tool selected to feed with data our system. For this task we develop  config_file, logstash_restaurantes.conf, in order to do it (LINUX):

$./bin/logstash -f ./config/ logstash_restaurantes.conf.conf --debug --verbose 
