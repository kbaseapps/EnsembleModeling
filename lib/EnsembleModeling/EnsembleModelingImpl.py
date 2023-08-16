# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class EnsembleModeling:
    '''
    Module Name:
    EnsembleModeling

    Module Description:
    A KBase module: EnsembleModeling
This module implements tools for estimating reaction probabilities from functional annotations, building ensemble models by sampling from those probabilities, and analyzing the results of the ensemble modeling
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def estimate_reaction_probabilities(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN estimate_reaction_probabilities
        #END estimate_reaction_probabilities

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method estimate_reaction_probabilities return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def build_ensemble_model(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN build_ensemble_model
        #END build_ensemble_model

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method build_ensemble_model return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def gapfill_ensemble_model(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN gapfill_ensemble_model
        #END gapfill_ensemble_model

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method gapfill_ensemble_model return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def run_ensemble_FBA(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_ensemble_FBA
        #END run_ensemble_FBA

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method run_ensemble_FBA return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def analyze_ensemble_modeling(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN analyze_ensemble_modeling
        #END analyze_ensemble_modeling

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method analyze_ensemble_modeling return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
