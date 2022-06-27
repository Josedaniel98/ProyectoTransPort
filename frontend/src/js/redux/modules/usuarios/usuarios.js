import {handleActions} from 'redux-actions';
import {createReducer} from "../baseReducer/baseReducer";


// ------------------------------------
// Constants
// ------------------------------------

export const { reducers, initialState, actions } = createReducer(
    "usuarios",
    "user",
    "EditarUsuarioForm",
    "/usuarios",
);

export default handleActions(reducers, initialState);
