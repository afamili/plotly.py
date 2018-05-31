import _plotly_utils.basevalidators


class DtickrangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='dtickrange',
        parent_name='layout.xaxis.tickformatstop',
        **kwargs
    ):
        super(DtickrangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks+margins',
            items=[
                {
                    'editType': 'ticks+margins',
                    'valType': 'any'
                }, {
                    'editType': 'ticks+margins',
                    'valType': 'any'
                }
            ],
            role='info',
            **kwargs
        )