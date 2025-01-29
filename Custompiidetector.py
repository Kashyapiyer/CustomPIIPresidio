from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import  AnonymizerEngine
import logging
logging.getLogger("presidio-analyzer").setLevel(logging.ERROR)

class Custompiidetectorandanonimizer: 
      def __init__(self,configobj) -> None:
          self.analyzer = AnalyzerEngine()
          self.anonymizer = AnonymizerEngine()
          self.score_threshold = configobj['score_threshold']
          self.language = configobj['language']
          self.allowedlist = configobj['targetlist']
          self.doanonymize = configobj.get('doanonymize', True)

      def customanalyzer(self, contextstr):
              try : 
                  response = {}
                  panalyzer = AnalyzerEngine()
                  #print(f"Considering denonymize {self.doanonymize}")
                  panonymizer = AnonymizerEngine()
                  results = panalyzer.analyze(text=contextstr, language=self.language, allow_list=self.allowedlist, score_threshold=self.score_threshold)
                  if self.doanonymize: 
                      panonymizeresult= panonymizer.anonymize(text=contextstr,analyzer_results=results)
                      panonymizeresulttext = panonymizeresult.text
                  else: 
                      panonymizeresulttext = None 
                  
                  if results:  
                    response['textdetected'],response['entitiesdetected']=[ ],[ ]
                    for entry in results:
                        response['textdetected'].append(contextstr[entry.start:entry.end])
                        response['entitiesdetected'].append(entry.entity_type)
                        response['score'] = entry.score
                        response['anonimizedtext'] = panonymizeresulttext
                        response['piidetected'] = True
                        response['contextsupplied'] = contextstr
                    return response
                  else:
                    response['piidetected'] = False
                    response['contextsupplied'] = contextstr
                    return response
              except Exception as e:
                  return f"Encountered Error while detecting pii  please find error as {e}"