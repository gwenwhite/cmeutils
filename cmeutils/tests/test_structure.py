import pytest

import numpy as np

from cmeutils.tests.base_test import BaseTest
from cmeutils.structure import gsd_rdf, get_quaternions

class TestStructure(BaseTest):
    def test_gsd_rdf(self, gsdfile_bond):
        rdf_ex, norm = gsd_rdf(gsdfile_bond, "A", "B")
        rdf_noex, norm2 = gsd_rdf(gsdfile_bond, "A", "B", exclude_bonded=False)
        assert norm2 == 1
        assert not np.array_equal(rdf_noex, rdf_ex)

    def test_gsd_rdf_samename(self, gsdfile_bond):
        rdf_ex, norm = gsd_rdf(gsdfile_bond, "A", "A")
        rdf_noex, norm2 = gsd_rdf(gsdfile_bond, "A", "A", exclude_bonded=False)
        assert norm2 == 1
        assert not np.array_equal(rdf_noex, rdf_ex)

    def test_get_quaternions(self):
        with pytest.raises(ValueError):
            get_quaternions(0)

        with pytest.raises(ValueError):
            get_quaternions(5.3)

        qs = get_quaternions()
        assert len(qs) == 20
        assert len(qs[0]) == 4