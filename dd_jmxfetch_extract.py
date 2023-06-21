import re
import string
def getMetricData () :
    filename = '/tmp/jem/dd_jmxfetch'
    metrics_out = ""
    with open(filename, 'r') as input:
         for line in input:
             if line.find('ConsoleReporter'):
                metric_name = (line.split("|")[-1]).split("[")[0]
                metric_data = ((line.split("|")[-1]).split("[")[-1]).split("=")[-1]
                metrics_out = metrics_out+metric_name+"="+metric_data+","
                #metrics=" ".join(metrics_out.split())
         #print(metrics.translate({ord(c): None for c in string.whitespace}))
         metrics=re.sub(r"\s+", "", metrics_out)[:-1]
    return metrics
                #for i in range(len(metric_name)):
                   #jmx_payload = jmx_payload+payload[i]+","
                   #print ("jmxHZ_Metrics,tag1=hazelcast"+" "+jmx_payload[:-1])
jmx_payload=getMetricData ()
print ("jmxTom_Metrics,tag1=Tomcat"+" "+jmx_payload)
