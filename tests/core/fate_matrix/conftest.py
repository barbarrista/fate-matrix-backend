from collections.abc import Mapping
from datetime import date

import pytest

from app.core.domain.fate_matrix.dto import PointBundleDTO


@pytest.fixture
def point_bundle_mapping() -> Mapping[date, PointBundleDTO]:
    return {
        date(1996, 4, 11): PointBundleDTO(
            a1=11,
            a2=3,
            a3=19,
            b1=4,
            b2=16,
            b3=12,
            c1=7,
            c2=22,
            c3=15,
            d1=22,
            d2=7,
            d3=3,
            e=8,
            f1=15,
            f2=10,
            f3=22,
            g1=11,
            g2=11,
            g3=18,
            h1=11,
            h2=11,
            h3=18,
            h4=11,
            i1=6,
            i2=19,
            i3=13,
            j1=21,
            j2=18,
            j3=6,
            k1=7,
            k2=15,
            l1=9,
            l2=20,
        ),
        date(1998, 3, 11): PointBundleDTO(
            a1=11,
            a2=5,
            a3=21,
            b1=3,
            b2=16,
            b3=13,
            c1=9,
            c2=10,
            c3=19,
            d1=5,
            d2=20,
            d3=15,
            e=10,
            f1=14,
            f2=21,
            f3=7,
            g1=12,
            g2=17,
            g3=5,
            h1=14,
            h2=21,
            h3=7,
            h4=3,
            i1=16,
            i2=7,
            i3=9,
            j1=22,
            j2=7,
            j3=8,
            k1=11,
            k2=21,
            l1=4,
            l2=5,
        ),
    }