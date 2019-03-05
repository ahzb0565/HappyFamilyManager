import { fetchFundList, addFund, deleteFund } from '@/services/api';

export default {
  namespace: 'fund',

  state: {
    list: [],
    details: {},
  },

  effects: {
    *fetchFunds({ payload }, { call, put }) {
      const response = yield call(fetchFundList, payload);
      yield put({
        type: 'saveList',
        payload: response,
      });
    },
    *addFund({ payload, callback }, { call, put }) {
      const response = yield call(addFund, payload);
      yield put({
        type: 'saveDetails',
        payload: response,
      });
      if (callback) callback();
    },
    *removeFund({ id, callback }, { call }) {
      yield call(deleteFund, id);
      if (callback) callback();
    },
  },

  reducers: {
    saveList(state, { payload }) {
      return {
        ...state,
        list: [...payload],
      };
    },
    saveDetails(state, { payload }) {
      return {
        ...state,
        details: { ...payload },
      };
    },
  },
};
