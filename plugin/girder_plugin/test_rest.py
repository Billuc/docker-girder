# -----------------------------------------------------------------------------
# Description : Submission Registry Model
# Author      : Tiphaine Diot <diot@creatis.insa-lyon.fr>
#
# -----------------------------------------------------------------------------


from girder.api.rest import Resource
from girder.api import access
from girder.api.describe import autoDescribeRoute, Description

class TestRest(Resource):
    def __init__(self):
        super().__init__()
        self.resourceName = "test"

        self.route("GET", (), self.test_route)

    @access.public
    @autoDescribeRoute(
            Description("test route").param(name="name", description="name", required=False, default="World")
            )
    def test_route(self, params):
        return {
            "status": 200,
            "message": f"Hello, {params['name']} !"
        }
