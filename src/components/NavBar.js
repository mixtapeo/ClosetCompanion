import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../default_icon-modified.png';

const NavBar = () => {
  return (
    <nav className=" p-8 bg-indigo-50 rounded-none flex items-center justify-between">
      <img src={logo} alt="Logo" className="h-14 w-14 mr-6 " />
      <span className="text-white text-2xl font-bold mr-auto">Closet Companion</span>
      <ul className="flex justify-center font-bold space-x-20  ">

        <li className="text-gray-200transition-transform transform hover:-translate-y-2 transition-all duration-300">
          <Link
            to="/"
          >
            Home
          </Link>
        </li>
        <li className="text-gray-200  transition-transform transform hover:-translate-y-2 transition-all duration-300">
          <Link
            to="/contact"

          >
            Outfits
          </Link>
        </li>
        <li className="text-gray-200 transition-transform transform hover:-translate-y-2 transition-all duration-300" >
          <Link
            to="/add"
          >
            Add
          </Link>
        </li>

      </ul>
      <div className="absolute left-0 right-0 bottom-0 h-1 bg-gray-500 transform scale-x-0 transition-transform duration-300 ease-in-out hover:scale-x-100" />
    </nav>

  )
}

export default NavBar;