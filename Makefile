.DEFAULT_GOAL = run

.PHONY: test
test:  
	@ py.test ${args} . 


.PHONY: clean
clean:  
	@ find . -name "*.pyc" -delete


.PHONY: requirements
requirements:
	@ bash -c "source ../system/bin/activate && pip install -r requirements.txt"


.PHONY: dependencies
dependencies:
	@ bash -c "source ../system/bin/activate && pip install cython"
