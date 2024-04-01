
# Женя Чабанов, 14 когорта, финальный проект, QA+

from create import create_order, get_order_by_track


def test_get_order_by_track():
    track = create_order()

    assert track is not None

    status_code, _ = get_order_by_track()

    assert status_code == 200