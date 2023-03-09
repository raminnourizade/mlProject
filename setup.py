from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requerments(file_path:str)->List[str]:
    ''' 
    this functon returns requerments for this package
    '''
    requerments=[]
    with open(file_path) as file_obj:
        requerments=file_obj.readlines()
        requerments=[req.replace("\n","") for req in requerments]
        if HYPEN_E_DOT in requerments:
            requerments.remove(HYPEN_E_DOT)
        return requerments





setup(
        name="mlProject", 
        version='0.0.1',
        author="Ramin Nourizadeh",
        author_email="ramin.nourizade@gmail.com",
        description='A Generic Structure for Machine Learning Projects',
        long_description='A Generic Structure for Machine Learning Projects',
        packages=find_packages(),
        
        install_requires=get_requerments('requirements.txt'), 
        
        keywords=['python', 'generic Structure']
       
)