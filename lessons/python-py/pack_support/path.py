import os, sys

class Project_Map():

    root = os.path.dirname(sys.argv[0])
    a = os.path.split(root)
     
    def __init__(self,r="/"):
        self.r = r

    def root_path (self):
        
        terek = "terek"

        # r = "salam " + self.root
        return self.r + terek


    #     self.a_root = a[0]
    #    # self.rp = self.a_root 
    #     return self.a_root

p1=Project_Map("Beka") 

print (  p1.root_path()  )

# class ProjectMap:
#     """provides convenient and consistent access to paths which are
#     necessary to the builds"""

#     def __init__(self):
#         """locate the build specification document, to use as a reference
#         point for all other paths"""
#         root = os.path.dirname(os.path.abspath(sys.argv[0]))
#         if "py.test" in sys.argv[0]:
#             root = os.getcwd()
#         while True:
#             build_spec = root + "/build_specification.xml"
#             if not os.path.exists(build_spec):
#                 if (os.path.dirname(root) == root):
#                     # we are at "/"
#                     assert(False)
#                     return

#                 root = os.path.dirname(root)
#                 continue

#             # else we have found the spec
#             self._source_root = root
#             break
#         # cache the current_project, because it can't be recalculated
#         # if the caller changes directories.
#         self._current_project = None
#         self._current_project = self.current_project()

#     def source_root(self):
#         """top directory, which contains the build_specification.xml"""
#         return self._source_root
