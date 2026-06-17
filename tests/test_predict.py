from src.predict import predict_yield


def test_predict_returns_float_in_range():
    result = predict_yield(22.0, 88.0, 920)
    assert isinstance(result, float)
    assert 0 < result < 50


def test_different_inputs_change_prediction():
    low = predict_yield(22.0, 75.0, 920)
    high = predict_yield(22.0, 92.0, 920)
    assert high != low