using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace PersonalSite.Pages
{
    public class BioModel : PageModel
    {
        public string bioParagraph { get; set; }

        public void OnGet()
        {
            try
            {
                bioParagraph = System.IO.File.ReadAllText("wwwroot/txt/bio/bio.txt");
            }
            catch (Exception e)
            {
                bioParagraph = "Couldn't load text...";
            }
        }
    }
}