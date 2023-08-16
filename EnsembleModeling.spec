/*
A KBase module: EnsembleModeling
This module implements tools for estimating reaction probabilities from functional annotations, building ensemble models by sampling from those probabilities, and analyzing the results of the ensemble modeling
*/

module EnsembleModeling {

  typedef UnspecifiedObject ReportResults;

  funcdef estimate_reaction_probabilities(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef build_ensemble_model(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef gapfill_ensemble_model(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef run_ensemble_FBA(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef analyze_ensemble_modeling(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

};
