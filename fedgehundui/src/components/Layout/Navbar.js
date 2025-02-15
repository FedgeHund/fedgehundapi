import React, { Fragment } from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { URL } from '../App.js';
import { Link } from 'react-router-dom';
import '../../../styles/navbar.css';
import logo from '../../../static/homepage/logo.png';
import { getCookie } from '../Helpers/getCookie';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Navbar() {
	const [navbar, setNavbar] = useState(false);
	const [firstname, setFirstname] = useState();
	const [errorMessage, seterrorMessage] = useState();

	const checkUser = async () => {
		await axios.get("http://" + URL + "/auth/user/", {
		},
			{
				headers: {
					"Content-Type": 'application/json'
				}
			}
		)
			.then(function (response) {
				if (response.status == 200) {
					// console.log(response);
					setFirstname(response.data.first_name);
				}
				else {
					//window.location = "http://127.0.0.1:8000/signin/"
					// console.log(response);
				}
			}).catch(error => {
				seterrorMessage(
					error
				)
			}
			)
	};

	useEffect(() => {
		checkUser();
	}, []);


	const handleSubmit = async (e) => {

		var csrftoken = getCookie('csrftoken');

		await axios.post("http://" + URL + "/auth/logout/", {
		},
			{
				headers: {
					"Content-Type": 'application/json',
					'X-CSRFToken': csrftoken
				}
			}
		)
			.then(function (response) {
				if (response.status == 200) {
					// console.log(response);
				}
				else {
					//window.location = "http://127.0.0.1:8000/signin/"
					// console.log(response);
				}
			}.bind(this))

		window.location = "http://" + URL + "/signin/"
	};

	const changeNavbarBackground = () => {
		if (window.scrollY >= 80) {
			setNavbar(true);
		} else {
			setNavbar(false);
		}
	}

	window.addEventListener('scroll', changeNavbarBackground);

	return (
		<Fragment>
			<nav className={navbar ? 'navbar active fixed-top shadow-sm' : 'navbar fixed-top'}>

				<Link to={"/"} className="offset-1 mrktdb_nav_logo"><img src={logo} alt="Logo" className="logo" /></Link>
				<Link to={"/"} className="MrktDB mr-auto">MrktDB</Link>

				<form className="form-inline">
					<div className="lookup_form_everywhere">
						<input className="form-control lookup" placeholder="Fund / Stock Lookup" />
						<button className="btn btn-outline-none search_btn" type="submit"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
					</div>
				</form>

				<div className="navbar-nav">
					<a className="nav-item filers" href="#">13F Filers</a>
				</div>

				{
					firstname ?
						<span></span>
						:
						<Link to={"/signup"} className="signup_nav">Sign Up</Link>
				}


				{
					firstname ?
						<span></span>
						:
						<Link to={"/signin"} className="signin_nav">Sign In</Link>
				}

				{
					firstname ?
						<Link to={"/"} className="signup_nav mr-2">Hi, {firstname}</Link>
						:
						<span></span>
				}

				{
					firstname ?
						<div className="navbar-nav">
							<a className="nav-item circle" href="#"><i className="fas fa-2x fa-circle"></i></a>
						</div>
						:
						<span></span>
				}


				{
					firstname ?
						<Link to={"/signup"} onClick={handleSubmit} className="signin_nav">Sign out</Link>
						:
						<span></span>
				}


				<div className="navbar-nav">

					<div id="menuToggle">
						<input type="checkbox" className="toggler" />
						<div className="hamburger">
							<div></div>
						</div>


						<div id="menu">
							<div className="hamburger_container">
								<div className="menu_box">
									<div className="row margin_small15">
										<div className="col-md-1 col-sm-2 col-4 margin_small10 logo_div">
											<img src="../../../static/homepage/logo2.png" alt="White logo" className="hamburger_white_logo" />
										</div>
										<div className="col-md-1 mrktdb_white col-2 margin_small10">
											MrktDB
									</div>
										<div className="offset-md-5 col-md-2 offset-sm-2 col-sm-2 col-4 margin_small10 signup_left">
											<a href="/signup" className="signup_menu">Sign Up</a>
										</div>
										<div className="col-md-2 col-sm-2 col-4 margin_small10 signup_left">
											<a href="/signin" className="signup_menu">Sign In</a>
										</div>
									</div>

									<div className="up_13f">
										<div className="row margin10">
											<div className="offset-md-2 col-md-1 menu_13f margin3">13F</div>
										</div>

										<div className="row margin6">
											<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">Latest Filings&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Searching&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>

										<div className="row">
											<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">Popular Stocks&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Fund Performance Search&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>

										<div className="row">
											<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Trends&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Stock Screener&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>

										<div className="row">
											<a href="#" className="filer_items offset-md-2 col-md-3 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Statistics&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>
									</div>

									<div className="row">
										<div className="horizontal_line margin10 offset-md-2 col-md-8 col-12 mb-2 horizontal_line_to_right"></div>
									</div>



									<div className="quick_links">
										<div className="row">
											<div className="footer_heading offset-2 col-2">Help</div>
											<div className="footer_heading col-2">Collaborate</div>
											<div className="footer_heading col-2">Connect</div>
											<div className="footer_heading col-2">Explore</div>
										</div>

										<div className="row hover_effect_row margin6">
											<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>Our offerings&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Advertise with us&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="/contactus" className="filer_items col-2 hover_effect"><div>Contact Us&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Email Newsletter&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>

										<div className="row hover_effect_row">
											<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>How MrktDB works?&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Business Resources&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Report a Bug&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Upcoming events&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
										</div>

										<div className="row hover_effect_row">
											<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>Getting started&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div>Sign in&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
										</div>

										<div className="row hover_effect_row">
											<a href="/faq" className="filer_items offset-2 col-2 hover_effect"><div>FAQ&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
											<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
										</div>
									</div>

									<div className="quick_links_small_screen">
										<div className="row">
											<div className="col-12 footer_section">Quick links</div>
										</div>
										<div className="row">
											<div className="horizontal_lines_small_screen col-12 mt-2 horizontal_lines_small_screen_to_right"></div>
										</div>

										<div className="row margin_small10">
											<div className="footer_heading col-6">Help</div>
											<div className="footer_heading col-6">Connect</div>
										</div>

										<div className="row margin_small6">
											<a href="#" className="filer_items col-6 hover_effect"><div>Our offerings</div></a>
											<a href="/contactus" className="filer_items col-6 hover_effect"><div>Contact Us</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>How MrktDB works?</div></a>
											<a href="#" className="filer_items col-6 hover_effect"><div>Report a Bug</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>Getting started</div></a>
											<a href="#" className="filer_items col-6 hover_effect"><div>Sign in</div></a>
										</div>

										<div className="row margin_small3">
											<a href="/faq" className="filer_items col-6 hover_effect"><div>FAQ</div></a>
										</div>


										<div className="row margin_small10">
											<div className="footer_heading col-6">Collaborate</div>
											<div className="footer_heading col-6">Explore</div>
										</div>

										<div className="row margin_small6">
											<a href="#" className="filer_items col-6 hover_effect"><div>Advertise with us</div></a>
											<a href="#" className="filer_items col-6 hover_effect"><div>Email Newsletter</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>Business Resources</div></a>
											<a href="#" className="filer_items col-6 hover_effect"><div>Upcoming events</div></a>
										</div>



										<div className="row margin_small10">
											<div className="footer_heading col-6">Social Media</div>
										</div>

										<div className="row margin_small6">
											<a href="#" className="filer_items col-6 hover_effect"><div>Twitter</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>Instagram</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>Facebook</div></a>
										</div>

										<div className="row margin_small3">
											<a href="#" className="filer_items col-6 hover_effect"><div>LinkedIn</div></a>
										</div>

										<div className="row margin_small10">
											<div className="horizontal_lines_small_screen col-12"></div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

			</nav>




		</Fragment>
	);
}

export default Navbar;
