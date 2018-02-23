import sys, os, re, glob
import ConfigParser
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))
import build_support as bs


class CaseConfig(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


tests = ["crucible-test","cts-test","deqp-test","glescts-test","piglit-test","vulkancts-test"]
# test = "deqp-test"

source_root  = bs.ProjectMap().source_root()
# print(source_root)


def get_conf_files(test):
    conf_dir = os.path.join(source_root,test)

################  uncomment by 1 at each run ################

    # config_path = glob.glob(conf_dir + "/*.conf")      # conf
    config_path = glob.glob(conf_dir + "/*.txt")      # blacklist
    # config_path = glob.glob(conf_dir + "*/*/*.txt")      #  expectations

    
    return config_path


def a_content(conf):
    if str(conf).endswith("conf"):
        content = """[expected-failures]

[expected-crashes]

[fixed-tests]"""
    # elif str(conf).endswith("expectations") or str(conf).endswith("txt"):
    elif str(conf).endswith("txt"):
        content = ""
    return content
        
        
        

def clean_conf_files(conf):
    
    with open(conf,"w") as file:
        file.write(a_content(conf))
        print("Done writing to the confog file")

# clean_conf_files(test)


def main():

    for test in tests:
        for conf in get_conf_files(test):       
                    
            clean_conf_files(conf)

        
            




if __name__ == "__main__":
    main()
