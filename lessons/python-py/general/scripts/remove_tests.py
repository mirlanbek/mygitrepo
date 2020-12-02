import sys, os, re
import ConfigParser
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))
import build_support as bs


class CaseConfig(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr

# put the commit needs to be removed
blame_test = "piglit 84c528875537237af5e942c4b9864cdbdc2aa782"

tests = ["crucible-test","cts-test","deqp-test","glescts-test","piglit-test","vulkancts-test"]
# tests = ["deqp-test"]

source_root  = bs.ProjectMap().source_root()

def remove_tests (sections):
    for a_test in tests:
        path_to_test =  source_root + "/" + a_test
        configs = []
        b_configs = os.listdir(path_to_test)
        for j in b_configs:
            if re.search("\w.*\.conf",str(j)):
                configs.append(j)
#        print(configs)        
                
        
        for config in configs:
            os.chdir(path_to_test)

            if os.path.exists(config):
                x = CaseConfig()
#                print(config)                            
                x.read(config)
                for o in (x.items(sections)):                    
#                 print(o)
                    if blame_test in o[1]:
                        
                        x.remove_option(sections,o[0])
                          
                    x.write(open(config,"w"))     
                   


def main():
    sec = ["expected-failures","expected-crashes","fixed-tests"]

    for k in sec[:2]:
        remove_tests(k)



if __name__ == "__main__":
    main()
