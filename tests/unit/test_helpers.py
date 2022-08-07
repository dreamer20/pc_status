from pc_status.helpers import timestamps_from_date_range, get_new_offset
import pytest

test_data_timestamps = [
    ('', '', None, None),
    ('2022-02-02', '2022-02-02', 1643760000.0, 1643846399.0),
    ('2022-02-02', '', 1643760000.0, None),
    ('', '2022-02-02', None, 1643846399.0),
    ('124 dsaf', 'asdf234', None, None)
]

test_data_offset = [
    (10, 0, 100, None, 10),
    (10, 100, 100, 90, None),
    (10, 90, 102, 80, 100),
    (10, 90, 100, 80, None),
    (10, 100, 102, 90, None),
]


@pytest.mark.parametrize(
    "from_date,"
    "to_date,"
    "expected_start_timestamp,"
    "expected_stop_timestamp",
    test_data_timestamps
)
def test_timestamps_from_date_range(from_date,
                                    to_date,
                                    expected_start_timestamp,
                                    expected_stop_timestamp):
    ''' Returns timestamp from date string or None '''
    start_timestamp, stop_timestamp = timestamps_from_date_range(
        from_date,
        to_date
    )

    assert start_timestamp == expected_start_timestamp
    assert stop_timestamp == expected_stop_timestamp


@pytest.mark.parametrize(
    "limit,"
    "offset,"
    "records_count,"
    "expected_prev_offset,"
    "expected_next_offset",
    test_data_offset
)
def test_get_new_offset(limit,
                        offset,
                        records_count,
                        expected_prev_offset,
                        expected_next_offset):
    ''' Returns calculated offset or None if offset isn't available '''
    prev_offset, next_offset = get_new_offset(limit, offset, records_count)

    assert prev_offset == expected_prev_offset
    assert next_offset == expected_next_offset
