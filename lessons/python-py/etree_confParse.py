import xml.etree.ElementTree as ET
import ConfigParser
import os, sys     

# xml_file = "dir_2/books.xml"
# x = ET.parse(xml_file)
# tests = x.findall("testsuites/testcase")        
# print([i.attrib['name']+":"+ i.attrib['classname']  for i in tests] )


class CaseConfig(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))

config_file_dir = os.getcwd()+"/test_dir/deqp-test"
test_file_dir = os.getcwd()+"/test_dir/test"


def remove_test (platform,arch):
    file_name = "piglit-deqp-test_{}_{}_0.xml".format(platform,arch)    
    full_path = os.path.abspath(os.path.join(test_file_dir, file_name))

    if os.path.exists(full_path):      
        x = ET.parse(full_path)
        tests = x.findall("testsuite/testcase")        
        test_names_suffix = [test.attrib["classname"] + "." + test.attrib["name"] for test in tests]
        test_names = [".".join(test.split(".")[:-1]) for test in test_names_suffix]
    
#        print(test_names)
       
        if arch == "m64":
            conf_file = "{}.conf".format(platform)
        elif arch == "m32":
            conf_file = "{}m32.conf".format(platform)    

#       config = ConfigParser.ConfigParser()
        config = CaseConfig()
#        config.readfp(open("/home/majanes/src/jenkins/deqp-test/skl.conf"))
        if os.path.exists(os.path.join(config_file_dir,conf_file)):
            config.readfp(open(os.path.join(config_file_dir,conf_file)))


            def fail_crash(failure):
                               
        
                fails = config.items(failure)
#               print(fails)
                
                for afail in fails:
                    if afail[0] not in test_names:
                        config.remove_option(failure, afail[0])
            
            
                with open("conf/"+conf_file,"w+") as mconf:
                    mconf.write("")
                    
                config.write(open("conf/"+conf_file, "w"))
            for y in ("expected-failures","expected-crashes"):
                fail_crash(y)     
        
    
    
#onp("bxt","m32")


system_hw=[] 
a = os.listdir(config_file_dir)
for i in a[:]:
    split_name = i.split(".") 
    #print(split_name)
    for k in split_name:
        if k == "conf":
            continue
        system_hw.append(k)
#print (system_hw)

piglit_tests =  os.listdir(test_file_dir)

deqp_tests = [ d_test for d_test in piglit_tests if "deqp" in d_test ]
#print(deqp_tests)

for i in deqp_tests[:]:
    for k in system_hw[:]:
        if str(k) in i:
 
            for arch in ("m64","m32"):

                remove_test(str(k),arch)



    
    # create a revisions.txt in the result path
    # for each project, get the name, git revision, and commit message
    # build a small text table in revisions.txt
    # change jenkins editable notification to attach revisions.txt
    # use RepoSet in repo_set.py
    #temp_repo_dir = "/home/tokonbekov/src/mesa_jenkins/repos"

    # git = repo.git
    # git.checkout('HEAD', b="my_new_branch")         # create a new branch
    # git.branch('another-new-one')
    # git.branch('-D', 'another-new-one')             # pass strings for full control over argument order
    # git.for_each_ref()
