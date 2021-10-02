﻿// StubFileBase.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Text;

namespace AssemblyCrawler.Support
{
	public abstract class StubFileBase
	{
		#region Constructor
		public StubFileBase(string filename)
		{
			Filename = filename;
		}
		#endregion

		#region Public Methods
		public abstract void Write();
		#endregion

		#region Public Properties
		public string Filename { get; }
		#endregion
	}
}
