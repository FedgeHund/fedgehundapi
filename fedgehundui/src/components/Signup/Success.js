import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';

export class FormPersonalDetails extends Component {

	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="main_div">
                    <div className="signup_box p-3 shadow mb-5">

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="success_content1 col-md-10 offset-md-1">Homepage</div>
                            </div>
                        </div>
                      
                    </div>	
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;