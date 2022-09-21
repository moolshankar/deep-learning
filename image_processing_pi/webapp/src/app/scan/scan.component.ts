import { Component, OnInit } from '@angular/core';
import { VisitorService } from '../visitor.service';
import { Observable, throwError } from 'rxjs';

@Component({
  selector: 'app-scan',
  templateUrl: './scan.component.html',
  styleUrls: ['./scan.component.css']
})
export class ScanComponent implements OnInit {

  constructor(private visitorService: VisitorService) {}

  ngOnInit(): void {
    console.log('====================================');
    console.log('This is init call');
    console.log('====================================');
    //this.saveDataset()
  }

  saveDataset(): void {
    console.log('Save dataset is called');
    this.visitorService.saveDataset().subscribe(data => console.log(data))
  }

}
