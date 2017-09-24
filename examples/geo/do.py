import time

from oottadao.main.api import Assembly, Component
from oottadao.lib.drivers.api import DOEdriver
from oottadao.lib.doegenerators.api import FullFactorial, Uniform
from oottadao.examples.simple.paraboloid import Paraboloid

from oottadao.lib.casehandlers.api import JSONCaseRecorder, BSONCaseRecorder


class Analysis(Assembly):

    def configure(self):

        self.add('paraboloid', Paraboloid())

        self.add('driver', DOEdriver())
        #There are a number of different kinds of DOE available in oottadao.lib.doegenerators
        self.driver.DOEgenerator = FullFactorial(10) #Full Factorial DOE with 10 levels for each variable
        self.driver.DOEgenerator = Uniform(1220) 

        #DOEdriver will automatically record the values of any parameters for each case
        self.driver.add_parameter('paraboloid.x', low=-75, high=75)
        self.driver.add_parameter('paraboloid.y', low=-75, high=75)
        #tell the DOEdriver to also record any other variables you want to know for each case
        self.driver.gear()
        self.driver.add_response('paraboloid.f_xy')
        self.driver.add_response('paraboloid.xy')

        self.recorders = [JSONCaseRecorder('doe.json'), BSONCaseRecorder('doe.bson')]


if __name__ == "__main__":

    import time
    import motorgs

    analysis = Analysis()

    tt = time.time()
    gear = ['1','2']
    analysis.run()

    

    print "Elapsed time: ", time.time()-tt, "seconds"

    print analysis.driver.case_inputs.paraboloid.x[:5]
